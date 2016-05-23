def prototype(name,bases,dict):
	cls = type(name, bases,dict)
	cls.prototype = cls
	return cls

__metaclass__ = prototype

from copy import deepcopy

class prototyped_object:
   def clone(self):
      c = self.prototype()
      c.__dict__ = deepcopy(self.__dict__)
      return c


class Char:
  toplevels = set()

  def __init__(self, val):
    self.char = val
    self.successors = set()
    if self not in self.toplevels:
      self.toplevels.add(self)
    else:
      self.__dict__ = (set([self]) & self.toplevels).pop().__dict__

  def set_toplevel(self):
    item = (self.toplevels | set([self])).pop()
    item.merge(self)
 #   print item
    self.toplevels.add(item)

  def merge(this, other):
    for x,y in zip(this.successors, other.successors):
      x.merge(y)
      x.successors = x.successors | y.successors

  def clone(self, val):
      c = self.prototype(val)
      return c
  def __hash__(self):
    return hash(self.char)
  def __cmp__(self, other):
    try:
      return cmp(self.char, other.char)
    except AttributeError:
      return cmp(self.char, other)
  def process_word(self, word):
    if self.char == word[0]:
      try:
        new = self.clone(word[1])
        if word[1] in self.successors:
          new = (set([word[1]]) | this.successors).pop()
        new.process_word(word[1:])
        self.successors.add(new)
      except IndexError:
        pass

  def print_(self, depth=0):
    print '-'*depth+self.char
    for i in self.successors:
      i.print_(depth+1)



def process_text(text):
  text = ( x.strip() for x in text.replace('\n', ' ').expandtabs().split(' ') if x.strip().isalpha() and len(x.strip()) > 1 )
  for i in text:
    x = Char(i[0])
    x.process_word(i)
#    x.set_toplevel()

import random
def randword():
  string = []
  x = random.choice(tuple(Char.toplevels))
  string.append(x.char)

  while x.successors:
    x = random.choice(tuple(x.successors))
    string.append(x.char)
  return ''.join(string)

import sys
string = file(sys.argv[1]).read()

process_text(string)
#[ q.print_() for q in Char.toplevels ]

#for x in range(10000):
while raw_input() != 'q':
	print randword()
