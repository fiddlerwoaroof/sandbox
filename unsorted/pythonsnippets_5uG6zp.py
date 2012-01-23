def strip_common_prefix(text):
	text = text.split('\n')
	def count_spaces(text):
		counter = 0 
		txt = text.expandtabs(2)
		while txt.startswith(' '):
			counter += 1
			txt = txt[1:]
		return counter, text
	text = [ count_spaces(x) for x in text ]
	prefix = min(x[0] for x in text)
	return '\n'.join(x[1][prefix:] for x in text)

