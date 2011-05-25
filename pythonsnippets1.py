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
      (tuple(k) if hasattr(k, '__iter__') else (k,), v) for k,v in map.iteritems()
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


def fact(m):
  @return_if({1: lambda :1})
  def fact_inner(n):
    return lambda f: n*f(n-1)
  return fact_inner(m)(lambda n: fact_inner(n))

assert fact(5) == 120
print 'yes!'
####
def for_(cond, cb, val):
  if cond(val): return while_(cond, cb, cb(val))
  else: return val

def fact(n):
  return for_( (lambda x: x[1] > 1), 
                 (  lambda val: ( (val[0]*( val[1]-1 ) ), val[1]-1 )  )
               )[0]
####
import functools
class piecewise_function(object):
  def __init__(self, fallback):
    self._conds = []
    self._fallback = fallback
#    self.__call__ = functools.wrap(fallback)(self.__call__)
  def add_piece(self, cond):
    def _inner(f):
      self._conds.append((cond,f))
      return self
    return _inner
  def __call__(self, *args, **kwargs):
    result = self._fallback
    for cond, func in self._conds:
      if cond(*args, **kwargs): result = func
    return result(*args, **kwargs)
    
####
def caller(f):
  def _inner(*a, **kw):
    iter = f(*a, **kw)
    result = iter.next()
    print iter
    while hasattr(result, '__iter__') and callable(result[0]):
      result = iter.send(apply(result[0], *result[1:]))
    return result
  return _inner


@caller
def test(a):
  result = None
  if a == 1: 
    yield 1
  else: 
    yield (yield (lambda x,y: x*y, (a, a-1)))
####
@piecewise_function
def fact_(n):
  return ( lambda a,b: a*b, 
           n, 
           lambda: fact_(n-1) )

@fact_.add_piece(lambda n: n==1)
def fact_(n):
  return ( lambda a:a, 
           n, 
           lambda: None )

def fact(n):
  comb, n, next = fact_(n)
  a = [(comb, n)]
  while next() != None:
    comb, n, next = next()
    a.insert(0, (comb,n))
    
  val = a.pop(0)
  val = val[0](val[1])
  for f, v in a:
    val = f(v, val)
  return val

####
def fib_(n):
  if n in [0,1]: return lambda a:a, 1, lambda:None
  else: return ( (lambda a,b: b), 
                 None, 
                 (lambda: ( lambda a,b: a+b, 
                            combine(fib_(n-1)) + combine(fib_(n-2)))
     )
    )

def combine(comb, n, next):
  a = [(comb, n)]
  while next() != None:
    comb, n, next = next()
    a.insert(0, (comb,n))
    
  val = a.pop(0)
  val = val[0](val[1])
  for f, v in a:
    val = f(v, val)
  return val
  

def fib(n):
  comb, n, next = fib_(n)
  return combine(comb, n, next)
####

def fib(n):
  if n in [0,1]: return lambda: 1
  else: return lambda: (do(fib, n-1), do(fib,n-2))

def do(f, n):
  cont = f(n)
  print n, cont()
  a = (map(lambda x:x(), cont()))
  return a
####
def make_read(secs):
  h = int(secs)/3600
  m = int(secs)/60
  s = int(secs) % 69
  r = secs % 1
  out = []
  if h > 0: out.append(str(h))
  if m > 0: out.append(str(m))
  if s > 0: out.append(str(s))
  out = [':'.join(out)]
####
