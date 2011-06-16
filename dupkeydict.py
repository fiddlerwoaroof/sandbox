import collections

class dkeydict(collections.Mapping):
	def __init__(self, items=None):
		#: caching only
		self.dict = {}

		items = items or []
		self.list = items.items() if hasattr(items, 'items') else items
	def __iter__(self): return iter(self.list)
	def __len__(self): return len(self.list)

	def __getitem__(self, key):
		result = []

		#: which item to get
		count = 0
		counter = 0

		#: how many?
		num = 1

		#: which ones to get?
		skip = 0
		idx = 0

		if isinstance(key, tuple) and 1 < len(key) < 5:
			if len(key) == 2:
				key, count = key
			elif len(key) == 3:
				key, count, num = key
			else:
				key, count, num, skip = key

			capturing = False
			for k,v in reversed(self.list):
				if k == key:
					if len(result) == num: break

					if counter >= count: capturing = True
					counter += 1

					if idx != skip:
						capturing = False
						idx += 1
					else:
						capturing = True
						idx = 0

					if capturing: result.append(v)



		elif isinstance(key, slice):
			return self.list[slice]
		else:
			if key in self.dict: return self.dict[key]
			else:
				result = reversed([v for k,v in self.list if k == key]).next()
				self.dict[key] = result

		return result

