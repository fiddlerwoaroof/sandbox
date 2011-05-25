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

    
