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