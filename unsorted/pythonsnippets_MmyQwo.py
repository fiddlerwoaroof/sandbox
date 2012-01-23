import itertools

def strip_common_prefix(text):
		text = text.expandtabs(2).split('\n')
		text = itertools.izip_longest(*text, fillvalue='')
		text = list(itertools.dropwhile(lambda x: set(x) == set(' '), text))
		return '\n'.join(''.join(x) for x in zip(*text))

print strip_common_prefix('''   \n   asdasd\n    asdasd\n   asdasdasd''')
