'''
Created on Dec 30, 2013

@author: Justin
'''

import pygame
import Cursor
import Text
from Constants import *

class TextField(object):
  
  def __init__(self, coordinates=(100,100), shape=(400,200), font=None):
    self.body = ''
    self.symbol_body = []
    self.first_dirt = 0 # a bound on the earliest possible change to body
    self.lines = ['']
    self.first_line = 0 # the number of the first line displayed
    self.cursor = Cursor.Cursor(self, 0)
    self.coordinates = coordinates
    self.shape = shape
    
    "set up font"
    if font is None:
      font = ("monospace", 15)
    self.font = font
    myfont = self.get_font()
    self.font_height = myfont.get_linesize()
    self.char_width = myfont.size('a')[0]
    self.maxWidth = self.shape[0]/self.char_width
    self.maxHeight = self.shape[1]/self.font_height
  
  "replaces text from start up until but not including end"
  def replace(self, start, end, text=''):
    self.body = self.body[:start] + text + self.body[end:]
    pass
    self.first_dirt = max(0, start - self.maxWidth)
  
  '''The font object is accessed in this way because it is unpicklable;
  This way, TextField has no font object as a member.'''
  def get_font(self):
    return pygame.font.SysFont(*self.font)
  
  def draw(self, screen):
    self.update_all_lines(self.maxWidth, self.maxHeight)
    loc1 = min(self.cursor.location, self.cursor.location2)
    loc2 = max(self.cursor.location, self.cursor.location2)
    for loc in xrange(loc1, loc2 + 1):
      self.draw_cursor(screen, loc)
    lines = self.lines[self.first_line:self.first_line + self.maxHeight]
    for i in xrange(len(lines)):
      line = lines[i]
      surface = self.get_font().render(line, 1, WHITE)
      screen.blit(surface, (self.coordinates[0], self.coordinates[1] + i*self.font_height))
  
  def draw_cursor(self, screen, location=None):
    if location is None:
      location = self.cursor.location
    line_number, line_idx = self.get_line_number(location)
    line_number -= self.first_line
    if line_number < 0:
      self.scroll_up(-line_number)
      line_number += -line_number
    elif line_number >= self.maxHeight:
      self.scroll_down(line_number - self.maxHeight + 1)
      line_number -= line_number - self.maxHeight + 1
    box = pygame.Rect(100 + line_idx*self.char_width, 100 + line_number*self.font_height, \
            self.char_width, self.font_height)
    pygame.draw.rect(screen, CURSOR_COLOR, box, 0)
  
  def scroll_down(self, distance=1):
    self.first_line = min(len(self.lines) - 1, self.first_line + distance)
    #self.first_line += distance
  
  def scroll_up(self, distance=1):
    self.first_line = max(0, self.first_line - distance)
    #self.first_line -= distance
  
  "less efficient than update_lines, but easier to keep bug free"
  def update_all_lines(self, maxWidth, maxHeight):
    self.lines = Text.get_lines(self.body, maxWidth, 1000000)
  
  "updates all dirty lines that precede or are part of the display"
  def update_lines(self, maxWidth, maxHeight):
    dirt_line_number, dirt_idx = self.get_line_number(self.first_dirt, maxWidth)
    self.lines = self.lines[:dirt_line_number] + \
    Text.get_lines(self.body[self.first_dirt - dirt_idx:], \
            maxWidth, self.first_line + maxHeight - dirt_line_number)
    self.first_dirt = len(self.body)
  
  "returns the line number and the location within that line"
  def get_line_number(self, location):
    j = location
    for i, line in enumerate(self.lines):
      if j < len(line):
        return (i, j)
      j -= len(line)
    
    j += len(line)
    if j < self.maxWidth:
      return (i, j)
    else:
      return (i + 1, 0) # it must be a cursor location








