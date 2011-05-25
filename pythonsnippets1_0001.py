def for_(cond, cb, val):

  if cond(val): return while_(cond, cb, cb(val))

  else: return val



def fact(n):

  return for_( (lambda x: x[1] > 1), 

                 (  lambda val: ( (val[0]*( val[1]-1 ) ), val[1]-1 )  )

               )[0]
