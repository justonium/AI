'''
Created on Jan 3, 2014

@author: Justin
'''

class Frame(object):
  
  def __init__(self):
    self.owner = None
  
  def add_owner(self, owner):
    self.owners.add(owner)
  
class Start(Frame):
  
  def delete_left(self):
    pass

class End(Frame):
  
  def delete_right(self):
    pass

class Phrase(Frame):
  
  def __init__(self, members):
    self.members = members
    self.owners = {}
    self.prev = set()
    self.next = set()
  
  def remove(self, member):
    pass

class Character(Frame):
  
  def __init__(self, symbol):
    self.symbol = symbol
    self.owners = {}
    self.prev = None
    self.next = None
  
  def delete_left(self):
    "remove the character and the left link from the passage"
    left_link = self.prev
    right_link = self.next
    pre = left_link.prev
    suc = self.next
    pre.next = right_link
    right_link.prev = pre
  
    "alert the owners of the change"
    for owner in self.owners:
      owner.remove(self)
  
  def delete_right(self):
    "remove the character and the left link from the passage"
    left_link = self.prev
    right_link = self.next
    pre = left_link.prev
    suc = self.next
    left_link.next = suc
    suc.prev = left_link
  
    "alert the owners of the change"
    for phrase in self.owners:
      phrase.remove(self)
    






