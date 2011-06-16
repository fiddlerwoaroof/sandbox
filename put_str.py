def put_str(store, str, v):
   cur = store
   for c in str:
      cur = cur.setdefault(c, {})
   cur.setdefault(str[-1], set()).add(v)

