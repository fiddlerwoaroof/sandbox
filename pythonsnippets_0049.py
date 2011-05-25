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


