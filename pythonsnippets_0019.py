wisted.spread import pb, jelly
from twisted.python import log
from twisted.internet import reactor

class LilyPond:
def setStuff(self, color, numFrogs):
self.color = color
self.numFrogs = numFrogs
def countFrogs(self):
print "%d frogs" % self.numFrogs


class CopyPond(LilyPond, pb.Copyable): pass

class Sender:
def __init__(self, pond):
self.pond = pond
def got_obj(self, remote):
self.remote = remote
d = remote.callRemote("takePond", self.pond)
d.addCallback(self.ok).addErrback(self.notOk)
def ok(self, response):
print "pond arrived", response
reactor.stop()
def notOk(self, failure):
print "error during takePond:"
if failure.type == jelly.InsecureJelly:
print " InsecureJelly"
else:
print failure
reactor.stop()
return None

def main():
from copy_sender import CopyPond  # so it's not __main__.CopyPond
pond = CopyPond()
pond.setStuff("green", 7)
pond.countFrogs()
# class name:
print ".".join([pond.__class__.__module__, pond.__class__.__name__])
sender = Sender(pond)
factory = pb.PBClientFactory()
reactor.connectTCP("localhost", 8800, factory)
deferred = factory.getRootObject()
deferred.addCallback(sender.got_obj)
reactor.run()

if __name__ == '__main__':
main()
####

def cmp_dicts(dct, dct1):
cp = set()
for k in dct.keys():
if dct[k] != dct1.get(k,None):
cp.add(k)
return cp

####
thelist = [1,2,3,4,5,6,7,8,9,8,7,7,6,5,3,2,1,0]
thelist.insert(0, len(thelist))
datasize = thelist[0]
i=j=1;
while j <= (datasize-1):
if thelist[j] == thelist[j+1]:
j+=1
continue
if i==j:
i+=1
j+=1
continue
thelist[i]=thelist[j]
i+=1
j+=1

####
genetics.py -- python/ga
python -i genetics.py
####
GOAL = 17
POP = 30
a = [encode(sensify_list(decode(get_n_genes()))) for x in range(POP)]
from functools import partial
cp = partial(compare_seqs, goal=GOAL)
a.sort(cp)
b = [evaluate(decode(x)) for x in a]
b
sorted(b)

a = [encode(sensify_list(decode(cross(*a[:2])))) for _ in range(POP)]
####
import datetime
import emen2.subsystems.serializable_class
reload(emen2.subsystems.serializable_class)
from emen2.subsystems.serializable_class import *
a = schedule()
a.add_param('microscope', 129)
a.add_param('startdate', datetime.datetime(2008,1,1))
a.add_param('microscope', db.getrecord(129,ctxid))
####
a = db.newrecord('folder')
a.commit()
a.commit()
a['folder_name'] = 'aasd'
a.commit()
####
a = db.getrecord(range(200,300))
[x['indexby'] for x in a]
for x in a: x['indexby'] = 'theteststring'

[x['indexby'] for x in a]
db.putrecord(a)
a = db.getrecord(range(200,300))
[x['indexby'] for x in a]
###
range(463,962)
###
db._DBProxy__ctxid = 'b85246688f24c14712e0a7dfb93413f5defd50c4'
db.getrecord(0)
db.checkcontext()
dbtree.get_children()
dbtree.get_children([1])
###
a = {
0: set([1, 14, 16, 17, 19, 20, 21, 22]),
1: set([2]),
2: set([]),
14: set([15]),
15: set([]),
16: set([18]),
17: set([]),
18: set([]),
19: set([]),
20: set([]),
21: set([]),
22: set([])
}
def lookup(lis, table):
cset = table[lis.pop(0)]
ckey = None
for x in lis[:-1]:
if x in cset:
ckey = x
cset = table[x]
print x, cset
else:
raise Exception()
if lis[-1] in cset:
key = lis[-1]
return key, table[key]
else:
raise Exception()

import UserDict
import operator
class Tree(object, UserDict.DictMixin):
def __init__(self, table, root):
self.key = root
self.filled = False
self.children = {}
if root in table:
result = []
for child in table[root]:
result.append((child, Tree(table, child)))
self.filled = True
self.children.update(result)

def __getitem__(self, key):
if hasattr(key, '__iter__'):
return self.find([self.key] + list(key))
return self.children[key]
def keys(self):
return self.children.keys()
def find(self, path):
if len(path) == 1:
return self
else:
value = self[path[1]]
if value is not None:
value = value.find(path[1:])
return value
def __str__(self):
return '\n'.join(self.mkstrtree(0))
def mkstrtree(self, level, space='--'):
result = [space*level+str(level+1)+space+str(self.key)]
for id, child in self.children.items():
result.extend(child.mkstrtree(level+1))
return result
def mktree(self):
result = {}
def setitem(dict, key, value): dict[key] = value
for key, value in self.children.items():
if value.filled:
setitem(result, key, value.mktree())
else:
setitem(result, key, None)
return result
def count(self):
return len(self) + reduce(operator.add,
[x.count() for x in self.children.values()],
0)


b = Tree(a, 135);print b
###
{
0: {
1:{
2: {}
},
14: {
15: {}
},
16:{
18: {}
},
17:{}
19:{}
20:{}
21:{}
22:{}
}
}

###
{0: set([1, 2, 3]), 1: set([2, 3, 4]), 2: set([3, 4, 5]), 3: set([4, 5, 6]), 4: set([5, 6, 7]), 5: set([8, 6, 7]), 6: set([8, 9, 7]), 7: set([8, 9]), 8: set([9]), 9: set([])}
###
import re
re.sub('&([^;]+);', r'&.\1.;', 'sdsfjsdlflsdfsdf&asdasd;dfsdfgsfdgfsd&dsfdsaf; &sfgfdgds;')
import htmlentitydefs
result = []
for x in a:
n = htmlentitydefs.codepoint2name.get(ord(x))
if n is not None: x = '&%s;' % n
result.append(x)
####
[htmlentitydefs.name2codepoint.get(y,y) for y in [x[1] or x[2] for x in re.findall('(&([^;]+);|([^&]))', a)]]
result = []
for x in _:
if isinstance(x, int): result.append(chr(x))
else: result.append(x)


''.join(result)
htmlentitydefs.codepoint2name[ord('&')]
###
class LazyLoad(object):
def __init__(self, __func_, *args, **kwargs):
self.__func = __func_
self.__args = list(args)
self.__kwargs = kwargs
def __get__(self, inst, cls):
tb = cls.__dict__
nm = [x for x in tb.keys() if id(tb[x]) == id(self)][0]
setattr(inst, nm, self.__func(*self.__args, **self.__kwargs))
return getattr(inst, nm)

def func(a,b,c):
print a,b,c
return a+b,c

class a(object):
b = LazyLoad(func, 1,2,3)
c = LazyLoad(func, 2,3,4)
d = LazyLoad(func, 3,4,5)
__e = LazyLoad(func, 4,5,6)
def __str__(self): return str(self.__e)
####
import HTMLParser
class TMP(HTMLParser.HTMLParser):
INI = 0
DIV = 1
OTH = 2
AST = 3
def __init__(self):
HTMLParser.HTMLParser.__init__(self)
self.links = [];self.__tmp = [];self.dbuf = '';self.__state = self.INI;self.level = 0
def handle_starttag(self, tag, attrs):
attrs = dict(attrs);self.level += 1
print '%stag: %r, attrs: %r, state: %r' % ('\t'*self.level, tag, attrs, self.__state),
if tag == 'div' and self.__state != self.DIV and attrs.get('class') == 'smallbox':
print 'useful div',
self.__state = self.DIV
elif tag == 'img' and self.__state == self.OTH:
print 'useful image',
self.__tmp.append(attrs['src'])
elif tag == 'a' and self.__state == self.DIV:
print 'useful link',
self.__tmp.append(attrs['href']);self.__state = self.OTH
print '..done'
def handle_endtag(self, tag):
print '%sclose tag: %r' % ('\t'*self.level, tag)
self.level -= 1
if tag == 'div' and self.__state == self.DIV:
if self.dbuf is not '':
self.__tmp.append(self.dbuf)
self.dbuf = ''
self.links.append(self.__tmp);self.__tmp = []
self.__state == self.INI
elif tag == 'a' and self.__state == self.OTH:
self.__state = self.DIV
if self.dbuf is not '':
self.__tmp.append(self.dbuf)
self.dbuf = ''
def handle_data(self, data):
if self.__state == self.OTH:
self.dbuf += data + ' '

####
import HTMLParser
class TMP(HTMLParser.HTMLParser):
INI = 0
DIV = 1
OTH = 2
def __init__(self):
HTMLParser.HTMLParser.__init__(self)
self.level = 0
def handle_starttag(self, tag, attrs):
attrs = dict(attrs);self.level += 1
print '%s%r: %r' % ('\t'*self.level, tag, attrs)
def handle_endtag(self, tag):
print '%sclose tag: %r' % ('\t'*self.level, tag)
self.level -= 1
def handle_data(self, data):
print '%sdata: %r' %('\t'*(self.level+1), data)


import mechanize
def show_site(url):
br = mechanize.Browser()
r = br.open(url)
print r.info()
_a = TMP()
_a.feed(r.read())
#return _a.links


a = filter(None, show_site(raw_input('url? ')))
####
def inst(func):
return func()


class IterDict(dict):
keylist = []
@staticmethod
def keylistiter_():
print IterDict.keylist
index = 0
while 1:
if index >= len(IterDict.keylist): index = 0
if not IterDict.keylist: break
yield IterDict.keylist[index]
index += 1
keylistiter = keylistiter_.__get__(1)()
@classmethod
def reset(cls): cls.keylistiter = cls.keylistiter_()
def __setitem__(self, name, value):
if name not in self.keylist:
self.keylist.append(name)
dict.__setitem__(self, name, value)
def __delitem__(self, name):
if name in self.keylist:
del self.keylist[self.keylist.index(name)]
dict.__delitem__(self, name)


import itertools


class CONT(object): pass


class PIDmanager(object):
queue = IterDict()
tasks = None
@inst
def pid_generator():
counter = 0
while 1:
yield counter
counter += 1
@classmethod
def put_task(self, task):
pid = self.pid_generator.next()
self.queue[pid] = task
print pid
if self.tasks == None:
self.queue.reset()
self.tasks = self.queue.keylistiter
self.tasks.next()
@classmethod
def run_task(self):
if self.tasks != None:
pid = self.tasks.next()
task = self.queue[pid]
if hasattr(task, '__iter__') and isinstance(task[0], CONT):
_, func, args, kwargs, cleanup = task
result = []
self.queue[pid] = func(*args, **kwargs)
cleanup()
return self.queue[pid]
else:
del self.queue[pid]
return task
@classmethod
def run_all(self):
try:
while 1: self.run_task()
except StopIteration:
self.queue.reset()
self.tasks == None


def print_many(gen, total=2000, count=0):
print gen.next(),
if count < total:
return CONT(), print_many, (gen,), dict(total=total, count=count+1), cleanup


def cleanup(): print


PIDmanager.put_task( (CONT(), print_many, (itertools.cycle('a'),), dict(total=10), cleanup) )
PIDmanager.put_task( (CONT(), print_many, (itertools.cycle('b'),), dict(total=10), cleanup) )
PIDmanager.run_task()
######
import functools

class Namespace(object):
def __init__(self):
self.__insts = {}
def _bind_class(self, name, bases, dict):
cls = type(name, bases, dict)
cls.__ns = self
def __init__(slf, *args, **kwargs):
self.__insts[id(slf)] = slf
cls.__init__(*args, **kwargs)
print cls.__init__
cls.__init__ = __init__
return cls
def __call__(self, func):
result = func
if not func.__name__.startswith('_'):
setattr(self, func.__name__, func)
result = None
return result
def __getattribute__(self, name):
result = object.__getattribute__(self, name)
if callable(result):
result=functools.partial(result, self.__inst)
return result




class NamespacedClass(object):
a = Namespace()
__metaclass__ = a._bind_class
@a
def b(self, test_arg):
print self, test_arg

######
a = db.newrecord('folder')
a.commit()
if type(_) != int: print '!!!!!!!!!!!!!!!!!!!!'
a.commit()
if _ is not 'No changes made': print '!!!!!!!!!!!!!!!!!!!!'
a['folder_name'] = 'aasd'
a.commit()

######
import abc
class Pipe(object):
__metaclass__ = abc.ABCMeta
@property
def file(self): return self.__file
def __init__(self, file, *args, **kw):
self.__file = file
self.__delim = '\n'
self.init(*args, **kw)
def init(self, *args, **kw): pass
#
def __getattribute__(self, name):
result = None
try:
result = object.__getattribute__(self, name)
except Exception, e:
try:
result = self.__file.__getattribute__(name)
except:
raise e
return result
#
def read(self, bytes=-1):
buf = self.process_chunk(self.__file.read(bytes))
return buf
#
@abc.abstractmethod
def process_chunk(self, chunk): return chunk



import re
class Grep(Pipe):
def init(self, regex, delim='\n', *_, **__):
self.__re = re.compile(regex)
self.__delim = delim
#
def process_chunk(self, chunk):
buf = chunk.split(self.__delim)
out = []
while buf:
line = buf.pop(0)
if self.__re.search(line):
out.append(line)
return self.__delim.join(out)
######
import functools
import collections
def instantiate(cls): return cls()

class Namespace(object):
def registry(name, bases, dict_):
cls = type(name, bases, dict_)
cls.__dict = {}
return cls
__metaclass__ = registry
def __init__(self, instance=None):
self.__dict__ = self.__dict
self.__inst = instance
self._init()
def _init(self): pass
def __get__(self, instance, owner):
result = type(self)(instance)
return result
def __check_inst(self):
if self.__inst is None:
raise AttributeError, 'this class is unbound, can\'t call methods'
def __getattribute__(self, name):
if not name.startswith('_'):
self.__check_inst()
result = object.__getattribute__(self, name)
if callable(result) and not name.startswith('_'):
result = functools.partial(result, self.__inst)
return result



class DB(object):
@instantiate
class record(Namespace):
@classmethod
def _init(self):
self.__value = 1
def get(self, db):
return self.__value
def set(self, db, value):
self.__value = value
def checkparam(self, db):
print db.param.get()
return db.param.get() == self.get()
@instantiate
class param(Namespace):
@classmethod
def _init(self):
self.__value = 1
def get(self, db):
db.othermethod(self.__value)
return self.__value
def set(self, db, value):
db.othermethod(self.__value)
self.__value = value
db.othermethod(self.__value)
def othermethod(self, value): print self, value
def recordget(self): return self.record.get()
def recordset(self, value): return self.record.set(value)
####
import functools

def memoize(func):
_cache = {}
class NULL:pass
NULL = NULL()
@functools.wraps(func)
def _inner(*args, **kwargs):
_kwargs = tuple(
(k, tuple(v) if hasattr(v, '__iter__') else v) for k,v in kwargs
)
value = _cache.get((args, _kwargs), NULL)
if value is NULL:
value = func(*args, **kwargs)
_cache[(args,_kwargs)] = value
return value
_inner.__enter__ = lambda *_: _inner
_inner.__exit__ = lambda *_: _cache.clear()
_inner.reset = _cache.clear
_inner.cache = _cache
_inner.orig = func
return _inner

class return_if(object):
def __init__(self, map):
self._map = dict(
(tuple(k) if hasattr(k, '__iter__') else (k,),v) for k,v in map.iteritems()
)
self._func = lambda x:x
def _inner(self, *args):
if args in self._map: return self._map[args]
else: return self._func(*args)
def __call__(self, func):
self._func = func
return self._inner


@memoize
@return_if({1: 1})
def fact(n):
return n*fact(n-1)


@return_if({(1,1): 2, (2,2): 3, (3,3):4})
def sum(a,b):
return a+b


@memoize
@return_if({1: 1,2: 1})
def fib(n):
if n < 1: raise ValueError, "not n >= 1"
else:
return fib(n-1) + fib(n-2)
####

def b(): return a(2)

def c(): return b()*3

def a(n):
if n==1:
return n
else:
return n*n-1


def d(a):
return


def e(a):
return

####

def f(h):
def g(n):
if n <= 1: return 1
else: return n*h(n-1)

#def e(h):
#  def

def Y(f):
def g(h):
def i(x):
return f(h(h))(x)
return i
return g(g)


@Y
def fib(f):
def _inner(n):
if n in range(2): return 1
else: return f(n-1) + f(n-2)
return _inner


import functools

def bounce(func):
@functools.wraps(func)
def _inner(arg):
result = func(arg)
return result(fact)
return _inner

class return_if(object):
def __init__(self, map):
self._map = dict(
(tuple(k) if hasattr(k, '__iter__') else (k,),v) for k,v in map.iteritems()
)
self._func = lambda x:x
def _inner(self, *args):
if args in self._map: return self._map[args]
else: return self._func(*args)
def __call__(self, func):
self._func = func
return self._inner
@bounce
@return_if({1: lambda _:1})
def fact(n):
return lambda x: n*x(n-1)

####
class Result(object):
def __repr__(self): return 'Result: %r' % self.v
def __init__(self, v): self.v = v

def wrapper(func):
def _inner(a):
results = []
results.append(func(a))
v = results[-1].next()
print v
while not isinstance(v, Result):
results.append(func(v))
v = results[-1].next()
print v
results.pop()
if not results: result = v
else:
result = results.pop().send(v.v)
while results:
result = results.pop().send(result.v)
return result.v
return _inner

####
gen = fib(2)
gen.next()
gen1 = fib(_)
gen1.next()
gen.send(_.v)
gen2 = fib(_)
gen2.next()
gen.send(_.v)
_.v
####
def wrapper(func):
def _inner(a):
results = []
results.append(func(a))
v = results[0].next()
idx = 0
while True:
if not isinstance(v, Result):
results.append(func(v))
idx = len(results) - 1
v = results[idx].next()
else:
del results[idx]
if len(results) == 0: break
else:
idx -= 1
v = results[idx].send(v.v)
return v.v
return _inner

@wrapper
def fact(a):
if a == 1:
yield Result(1)
yield Result(a * (yield a-1))

@wrapper
def count(a):
if a == []: yield Result(0)
else:
yield Result(1 + (yield a[1:]))

@wrapper
def fib(a):
if a in [1,2]: yield Result(1)
else:
z = (yield a-1)
b = (yield a-2)
yield Result( z + b )

@wrapper
def fib(a):
if a in [1,2]: yield Result(1)
else:
z = (yield a-1)
b = (yield a-2)
yield Result( z + b )


@wrapper
def reverse(lis):
if lis == []: yield Result([])
else:
yield Result( [(yield lis[1:]), lis[0]] )