a = Database.User(dict(name=['Joe', '', 'Bloggs'], username='jblog', password='apassword', groups=[0]))
db.adduser(a)
db.approveuser(a.username,ctxid)
db.secrecordadduser ( ((a.username,),)*4, 125, ctxid=ctxid, recurse=3)