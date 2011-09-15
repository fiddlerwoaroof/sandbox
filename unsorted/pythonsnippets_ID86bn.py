def organize(tree, key):
	if key is None: return []
	result = [key, []]
	for k in tree.get(key, [None]):
		result[-1].append(organize(tree, k))
	return result

