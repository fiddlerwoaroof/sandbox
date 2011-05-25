

def newfolder(name, parent):

    a = db.newrecord('folder', ctxid)

    a['folder_name'] = name

    db.pclink(parent, a.commit(), ctxid=ctxid)
