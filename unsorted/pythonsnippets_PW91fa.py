@contextlib.contextmanager
def dict_munger(d):
	class Munger(object):
		def __getattribute__(self, k):
			return lambda v: d.__setitem__(k,v)
	yield Munger()





