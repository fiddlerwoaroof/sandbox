a = db.getrecord(range(200,300))

[x['indexby'] for x in a]

for x in a: x['indexby'] = 'theteststring'



[x['indexby'] for x in a]

db.putrecord(a)

a = db.getrecord(range(200,300))

[x['indexby'] for x in a]
