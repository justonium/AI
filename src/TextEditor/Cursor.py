'''
Created on Dec 31, 2013

@author: Justin
'''

import Text

class MasterCursor(object):
  
  def __init__(self):
    self.cursors = set()
  
  def clearCursors(self):
    self.cursors = set()
  
  def addCursor(self, cursor):
    self.cursors.add(cursor)
  
  def removeCursor(self, cursor):
    self.cursors.remove(cursor)
  
  def copy(self):
    pass
  
  def go_left(self):
    for cursor in self.cursors:
      cursor.go_left()
  
  def hilight_left(self):
    for cursor in self.cursors:
      cursor.hilight_left()
  
  def go_right(self):
    for cursor in self.cursors:
      cursor.go_right()
  
  def hilight_right(self):
    for cursor in self.cursors:
      cursor.hilight_right()
  
  def go_left_end(self):
    for cursor in self.cursors:
      cursor.go_left_end()
  
  def hilight_left_end(self):
    for cursor in self.cursors:
      cursor.hilight_left_end()
  
  def go_right_end(self):
    for cursor in self.cursors:
      cursor.go_right_end()
  
  def hilight_right_end(self):
    for cursor in self.cursors:
      cursor.hilight_right_end()
  
  def go_down(self):
    for cursor in self.cursors:
      cursor.go_down()
  
  def go_up(self):
    for cursor in self.cursors:
      cursor.go_up()
  
  def write(self, character):
    for cursor in self.cursors:
      cursor.write(character)
  
  def delete_left(self):
    for cursor in self.cursors:
      cursor.delete_left()
  
  def delete_right(self):
    for cursor in self.cursors:
      cursor.delete_right()

class Cursor(object):
  
  def __init__(self, textField, location=0):
    self.data = textField
    self.location = location
    self.location2 = location
  
  def go_left(self):
    if self.location > 0:
      self.location -= 1
      self.location2 = self.location
  
  def hilight_left(self):
    if self.location2 > 0:
      self.location2 -= 1
  
  def go_right(self):
    if self.location < len(self.data.body):
      self.location += 1
      self.location2 = self.location
  
  def hilight_right(self):
    if self.location2 < len(self.data.body):
      self.location2 += 1
  
  def go_left_end(self):
    self.go_left()
    while not self._left_of_word() and not self._right_of_word():
      self.go_left()
    self.location2 = self.location
  
  def hilight_left_end(self):
    self.hilight_left()
    while not self._left_of_word() and not self._right_of_word():
      self.hilight_left()
  
  def go_right_end(self):
    self.go_right()
    while not self._left_of_word() and not self._right_of_word():
      self.go_right()
    self.location2 = self.location
  
  def hilight_right_end(self):
    self.hilight_right()
    while not self._left_of_word() and not self._right_of_word():
      self.hilight_right()
  
  def _left_of_word(self):
    return self.location > 0 and self.location < len(self.data.body) \
            and self.data.body[self.location] in Text.delimiters \
            and self.data.body[self.location - 1] not in Text.delimiters \
            or self.location == 0
  
  def _right_of_word(self):
    return self.location < len(self.data.body) - 1 \
            and self.data.body[self.location] in Text.delimiters \
            and self.data.body[self.location + 1] not in Text.delimiters \
            or self.location == len(self.data.body)
  
  def go_down(self):
    pass
  
  def go_up(self):
    pass
  
  def write(self, character):
    assert len(character) == 1
    self.data.replace(self.location, self.location, character)
    self.location += 1
  
  def delete_left(self):
    self.data.replace(self.location - 1, self.location)
    self.location = max(0, self.location - 1)
  
  def delete_right(self):
    self.data.replace(self.location, self.location + 1)















