'''
Created on Dec 30, 2013

@author: Justin
'''

import cPickle
import os

def safe_dump(path, objectName, obj):
  extension = '_tmp'
  while True:
    try:
      dump(path, objectName + extension, obj)
      load(path, objectName + extension)
      break
    except:
      pass
  if os.path.exists(os.path.join(path, objectName) + '.pkl'):
    os.remove(os.path.join(path, objectName) + '.pkl')
  os.rename(os.path.join(path, objectName) + extension + '.pkl', os.path.join(path, objectName) + '.pkl')

def dump(path, objectName, obj):
  f = open(os.path.join(path, objectName + '.pkl'), 'wb')
  cPickle.dump(obj, f)
  f.close()

def load(path, objectName):
  f = open(os.path.join(path, objectName + '.pkl'), 'rb')
  res = cPickle.load(f)
  f.close()
  return res