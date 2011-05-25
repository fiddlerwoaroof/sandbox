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