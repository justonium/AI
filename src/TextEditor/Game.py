'''
Created on Dec 30, 2013

@author: Justin
'''

import sys
import os
import IO
import TextField
import pygame
from Keys import *
from Constants import *
import Cursor
import DataObject
from collections import defaultdict as defaultdict

'''There are multiple cursors--one in each TextField.
This doesn't get updated in the dictionary.
There should be one master cursor which jumps between these cursors.'''

"save and exit"
def quitGame(path):
  IO.safe_dump(path, 'data', data)
  sys.exit(0)

"create the screen"
pygame.init()
from pygame.locals import *
screen = pygame.display.set_mode((600, 400))
#screen = pygame.display.set_mode((1024, 768), FULLSCREEN) #debug

"set key repeat"
pygame.key.set_repeat(150, 20)

"load data object"
path = sys.argv[1]
datapath = os.path.join(path, 'data.pkl')
if (os.path.exists(datapath)):
  data = IO.load(path, 'data')
else:
  data = DataObject.DataObject()
  data.textFields = [TextField.TextField()]
  filepath = os.path.join(path, 'files')
  if not os.path.exists(filepath):
    os.mkdir(filepath)

"create text field"
textFields = data.textFields
textField_index = len(textFields) - 1

"initialize cursor"
global cursor
cursor = Cursor.MasterCursor()
cursor.addCursor(textFields[textField_index].cursor)

def createTextField():
  textFields.append(TextField.TextField())

def load_prevTextField():
  global textField_index
  textField_index = max(0, textField_index - 1)
  global cursor
  cursor.clearCursors()
  cursor.addCursor(textFields[textField_index].cursor)

def load_nextTextField():
  global textField_index
  textField_index = min(len(textFields) - 1, textField_index + 1)
  global cursor
  cursor.clearCursors()
  cursor.addCursor(textFields[textField_index].cursor)

"initialize clock"
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30

"initialize typing mode"
global mode
mode = INSERT

"mode switching functions"
def go_normal():
  global mode
  mode = NORMAL

def go_insert():
  global mode
  mode = INSERT
  global cursor
  cursor.go_right()

def go_append():
  global mode
  mode = INSERT

def go_visual():
  global mode
  mode = VISUAL

char_ALL = defaultdict(lambda :None)
char_ALL.update({ \
        K_BACKSPACE:cursor.delete_left, combo(K_SHIFT, K_BACKSPACE):cursor.delete_right, \
        K_DELETE:cursor.delete_right, \
        K_LEFT:cursor.go_left, \
        K_RIGHT:cursor.go_right, \
        K_UP:textFields[textField_index].scroll_up, \
        K_DOWN:textFields[textField_index].scroll_down, \
        combo(K_CTRL, K_n):createTextField, \
        })

char_NORMAL = defaultdict(lambda :None)
char_NORMAL.update(char_ALL)
char_NORMAL.update({ \
        K_i:go_insert, \
        K_e:go_append, \
        K_h:cursor.go_left, combo(K_SHIFT, K_h):cursor.hilight_left, \
        K_l:cursor.go_right, combo(K_SHIFT, K_l):cursor.hilight_right, \
        K_j:cursor.go_down, \
        K_k:cursor.go_up, \
        K_g:cursor.go_right_end, combo(K_SHIFT, K_g):cursor.hilight_right_end, \
        K_s:cursor.go_left_end, combo(K_SHIFT, K_s):cursor.hilight_left_end, \
        combo(K_SHIFT, K_s):load_prevTextField, \
        combo(K_SHIFT, K_g):load_nextTextField, \
        })

char_INSERT = defaultdict(lambda :None)
char_INSERT.update(char_ALL)
char_INSERT.update({ \
        K_q:'q', combo(K_SHIFT, K_q):'Q', \
        K_w:'w', combo(K_SHIFT, K_w):'W', \
        K_e:'e', combo(K_SHIFT, K_e):'E', \
        K_r:'r', combo(K_SHIFT, K_r):'R', \
        K_t:'t', combo(K_SHIFT, K_t):'T', \
        K_y:'y', combo(K_SHIFT, K_y):'Y', \
        K_u:'u', combo(K_SHIFT, K_u):'U', \
        K_i:'i', combo(K_SHIFT, K_i):'I', \
        K_o:'o', combo(K_SHIFT, K_o):'O', \
        K_p:'p', combo(K_SHIFT, K_p):'P', \
        K_a:'a', combo(K_SHIFT, K_a):'A', \
        K_s:'s', combo(K_SHIFT, K_s):'S', \
        K_d:'d', combo(K_SHIFT, K_d):'D', \
        K_f:'f', combo(K_SHIFT, K_f):'F', \
        K_g:'g', combo(K_SHIFT, K_g):'G', \
        K_h:'h', combo(K_SHIFT, K_h):'H', \
        K_j:'j', combo(K_SHIFT, K_j):'J', \
        K_k:'k', combo(K_SHIFT, K_k):'K', \
        K_l:'l', combo(K_SHIFT, K_l):'L', \
        K_z:'z', combo(K_SHIFT, K_z):'Z', \
        K_x:'x', combo(K_SHIFT, K_x):'X', \
        K_c:'c', combo(K_SHIFT, K_c):'C', \
        K_v:'v', combo(K_SHIFT, K_v):'V', \
        K_b:'b', combo(K_SHIFT, K_b):'B', \
        K_n:'n', combo(K_SHIFT, K_n):'N', \
        K_m:'m', combo(K_SHIFT, K_m):'M', \
        K_BACKQUOTE:'`', combo(K_SHIFT, K_BACKQUOTE):'~', \
        K_1:'1', combo(K_SHIFT, K_1):'!', \
        K_2:'2', combo(K_SHIFT, K_2):'@', \
        K_3:'3', combo(K_SHIFT, K_3):'#', \
        K_4:'4', combo(K_SHIFT, K_4):'$', \
        K_5:'5', combo(K_SHIFT, K_5):'%', \
        K_6:'6', combo(K_SHIFT, K_6):'^', \
        K_7:'7', combo(K_SHIFT, K_7):'&', \
        K_8:'8', combo(K_SHIFT, K_8):'*', \
        K_9:'9', combo(K_SHIFT, K_9):'(', \
        K_0:'0', combo(K_SHIFT, K_0):')', \
        K_MINUS:'-', combo(K_SHIFT, K_MINUS):'_', \
        K_EQUALS:'=', combo(K_SHIFT, K_EQUALS):'+', \
        K_LEFTBRACKET:'[', combo(K_SHIFT, K_LEFTBRACKET):'{', \
        K_RIGHTBRACKET:']', combo(K_SHIFT, K_RIGHTBRACKET):'}', \
        K_BACKSLASH:'\\', combo(K_SHIFT, K_BACKSLASH):'|', \
        K_SEMICOLON:';', combo(K_SHIFT, K_SEMICOLON):':', \
        K_QUOTE:'\'', combo(K_SHIFT, K_QUOTE):'"', \
        K_COMMA:',', combo(K_SHIFT, K_COMMA):'<', \
        K_PERIOD:'.', combo(K_SHIFT, K_PERIOD):'>', \
        K_SLASH:'/', combo(K_SHIFT, K_SLASH):'?', \
        K_TAB:'\t', \
        K_RETURN:'\r', \
        K_SPACE:' ', \
        K_ESCAPE:go_normal, \
        })

char_VISUAL = defaultdict(lambda :None)

charmap = (char_INSERT, char_NORMAL, char_VISUAL)

"handler for game events"
def handle_keyboard_event(event, cursor):
  combo = get_key_combo(event)
  action = charmap[mode][combo]
  if action is None:
    return
  if type(action) == str:
    cursor.write(action)
  else:
    action()

"Main loop"
while True:
  
  "Draw to the screen."
  pygame.display.flip()
  dt = clock.tick(FRAMES_PER_SECOND)
  
  for event in pygame.event.get():
    "quit the game"
    if event.type == QUIT or exit(event):
      quitGame(path)
    
    "prepare to redraw"
    screen.fill(BLACK)
    
    "handle keyboard events"
    if hasattr(event, 'key'):
      down = event.type == KEYDOWN # key down or up?
      if down:
        handle_keyboard_event(event, cursor)
    
    "draw the text and cursor"
    textFields[textField_index].draw(screen)















