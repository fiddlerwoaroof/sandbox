import emen2.db.load as l
import emen2.db.config as cfg

cfg.gg.EMEN2DBHOME='/tmp/db'

dbo = cfg.DBOptions()
dbo.parse_args()
db = dbo.opendb()

with db:
	l.setup(rootpw='rootpw', rootemail='root@example.com', db=db)
