import datetime
import emen2.subsystems.serializable_class
reload(emen2.subsystems.serializable_class)
from emen2.subsystems.serializable_class import *
a = schedule()
a.add_param('microscope', 129)
a.add_param('startdate', datetime.datetime(2008,1,1))
a.add_param('microscope', db.getrecord(129,ctxid))