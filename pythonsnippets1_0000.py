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
