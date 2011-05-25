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
