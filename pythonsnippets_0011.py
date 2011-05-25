import ipc;reload(ipc)
import test_ipc;reload(test_ipc)
from ipc import *;from test_ipc import *
buf=Buf();a=Transport(buf);b=Transport(buf)
[x for x in a.send('hello')]