import itertools
def dict_merge(dct1, dct2):
	commonkeys = set(dct1) & set(dct2)
	newkeys = set(dct2) - commonkeys

	for key in commonkeys:
		olditem = dct1[key]
		newitem = dct2[key]
		if hasattr(newitem, 'items') and hasattr(olditem, 'items'):
			dict_merge(olditem, newitem)
		elif hasattr(olditem, 'update') and hasattr(newitem, '__iter__'):
			olditem.update(newitem)
		elif hasattr(olditem, 'extend') and hasattr(newitem, '__iter__'):
			olditem.extend(newitem)
		else:
			dct1[key] = dct2[key]
	dct1.update( (k,dct2[k]) for k in newkeys )
	return dct1


class _Null: pass
class Hier(object):
	####################
	# Class Attributes #
	####################

	@classmethod
	def init(cls):
		if not hasattr(cls, 'hier'):
			cls.hier = {}

	@classmethod
	def from_dict(cls, dct):
		cls.init()
		dict_merge(cls.hier, dct)
		return cls()

	#######################
	# Instance Attributes #
	#######################

	def __init__(self, name=''):
		self.init()

		self._name = name

		self._values = self.hier
		for segment in self._name.split('.'):
			item = self._values.get(segment)
			if hasattr(item, 'items'):
				print item
				self._values = item
			elif name != '':
				raise ValueError('no such item: %r' % self._name)

	def __getattribute__(self, name):
		try:
			return object.__getattribute__(self, name)
		except AttributeError:
			if name in self._values:
				result = self._values[name]
				if hasattr(result, 'items'):
					if self._name == '': result = Hier(name)
					else: result = Hier('%s.%s' % (self._name, name))
				return result
			else:
				raise




