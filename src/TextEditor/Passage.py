'''
Created on Jan 3, 2014

@author: Justin
'''

from Frame import *

'''There are multiple cursors. A Writer is a line which is used to insert text.
A Reacer is a rectangle which can be moved around over text.'''

class Passage(object):
  
  def __init__(self):
    "set up start and end characters"
    self.start = Start()
    self.end = End()
    
    "set up link between start and end"
    link = Link(self.start, self.end)
    
    "set up writer at the link"
    self.writer = Writer(link)

class Link(object):
  
  def __init__(self, prev, next):
    self.prev = prev
    self.next = next
    prev.next = self
    next.prev = self
  
  "inserts a frame at this link and returns the newly adapted left and right links on the frame"
  def insert(self, frame):
    pre = self.prev
    suc = self.next
    link2 = Link(frame, suc)
    self.next = frame
    frame.prev = self
    return self, link2

class Writer(object):
  
  def __init__(self, link):
    self.link = link
  
  "writes a character to the link that the writer is located at"
  def write(self, character):
    C = Character(character)
    _, self.link = self.link.insert(C)
  
  def delete_left(self):
    self.prev.delete_left()
  
  def delete_right(self):
    self.next.delete_right()
  
  "go to the previous link"
  def go_left(self):
    next = self.link.next.next
    if next is not None:
      self.link = next
  
  "go to the next link"
  def go_right(self):
    prev = self.link.prev.prev
    if prev is not None:
      self.link = prev















