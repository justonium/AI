'''
Created on Jan 1, 2014

@author: Justin
'''

delimiters = set([' ', '\t', '\r'])

def get_lines(text, maxLength, maxHeight):
  lines = []
  start = 0
  end = -1
  for i in xrange(len(text)):
    "update end"
    if text[i] == ' ':
      end = i
    
    "break off a line when needed"
    length = i - start
    if length >= maxLength:
      if end < start:
        lines.append(text[start:i])
        start = i
      else:
        lines.append(text[start:end] + ' ')
        start = end + 1
    elif text[i] == '\r':
      lines.append(text[start:i] + ' ')
      start = i + 1
    
    if len(lines) == maxHeight:
      return lines
  
  "break off the last line (even if it's empty)"
  lines.append(text[start:])
  
  return lines
      