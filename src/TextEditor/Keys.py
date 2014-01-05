'''
Created on Dec 30, 2013

@author: Justin
'''

import pygame
from pygame.locals import *

ALT = [K_LALT, K_RALT]
CTRL = [K_LCTRL, K_RCTRL]
SHIFT = [K_LSHIFT, K_RSHIFT]

K_ALT = -1
K_CTRL = -2
K_SHIFT = -3
COMBO_KEYS = set([K_LALT, K_RALT, K_LCTRL, K_RCTRL, K_LSHIFT, K_RSHIFT])

'''A key combination in index form is defined as follows:
If there are no keys already held, it is just the pressed key's number.
If there are keys already held, it is a tuple of the set of held keys' numbers and the pressed key.'''

'''get the key combination of an event in index form'''
def get_key_combo(event):
  assert event.type == KEYDOWN
  pressed_vec = pygame.key.get_pressed()
  pressed_keys = set([i for i, elem in enumerate(pressed_vec) if elem])
  if event.key in pressed_keys: #just in case the KEYDOWN event was generated artificially
    pressed_keys.remove(event.key)
  
  pressed_keys = pressed_keys.intersection(COMBO_KEYS)
  
  if not pressed_keys:
    return event.key
  
  "map all possible combinations of duplicated keys to a common set"
  if K_LALT in pressed_keys:
    pressed_keys.remove(K_LALT)
    pressed_keys.add(K_ALT)
  if K_RALT in pressed_keys:
    pressed_keys.remove(K_RALT)
    pressed_keys.add(K_ALT)
  if K_LCTRL in pressed_keys:
    pressed_keys.remove(K_LCTRL)
    pressed_keys.add(K_CTRL)
  if K_RCTRL in pressed_keys:
    pressed_keys.remove(K_RCTRL)
    pressed_keys.add(K_CTRL)
  if K_LSHIFT in pressed_keys:
    pressed_keys.remove(K_LSHIFT)
    pressed_keys.add(K_SHIFT)
  if K_RSHIFT in pressed_keys:
    pressed_keys.remove(K_RSHIFT)
    pressed_keys.add(K_SHIFT)
  
  return (frozenset(pressed_keys), event.key)

"maps from lists of key combinations to the form of key combinations used as indexes"
def combo(*keys):
  return (frozenset(keys[:-1]), keys[-1]) if len(keys) > 1 else keys[0]

"makes a detector for a a key combination defined by a list of keys"
def key_combo(keys):
  def _key_combo(event):
    return event.type == KEYDOWN and event.key == keys[-1] and keys_pressed(keys)
  return _key_combo

"detects if the provided list of keys are all pressed"
def keys_pressed(keys):
  pressed = pygame.key.get_pressed()
  if sum(pressed) != len(keys):
    return False
  for key in keys:
    if not key_pressed(key):
      return False
  return True

"detects if a key is pressed"
def key_pressed(key):
  pressed = pygame.key.get_pressed()
  if type(key) == int:
    return pressed[key]
  else:
    for k in key:
      if pressed[k]:
        return True
    return False

"some key combination detectors"
exit = key_combo([ALT, K_F4])
escape = key_combo([K_ESCAPE])


















