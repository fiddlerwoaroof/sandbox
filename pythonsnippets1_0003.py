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
