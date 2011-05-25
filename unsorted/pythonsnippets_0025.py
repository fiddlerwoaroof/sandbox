a = db.newrecord('folder')
a.commit()
a.commit()
a['folder_name'] = 'aasd'
a.commit()