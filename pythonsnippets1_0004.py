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
