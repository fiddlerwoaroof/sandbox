
def fib(n):
  if n in [0,1]: return lambda: 1
  else: return lambda: (do(fib, n-1), do(fib,n-2))

def do(f, n):
  cont = f(n)
  print n, cont()
  a = (map(lambda x:x(), cont()))
  return a