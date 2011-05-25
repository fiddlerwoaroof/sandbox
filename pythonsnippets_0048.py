
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
