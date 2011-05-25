import HTMLParser

class TMP(HTMLParser.HTMLParser):

	INI = 0

	DIV = 1

	OTH = 2

	def __init__(self):

		HTMLParser.HTMLParser.__init__(self)

		self.level = 0

	def handle_starttag(self, tag, attrs):

		attrs = dict(attrs);self.level += 1

		print '%s%r: %r' % ('\t'*self.level, tag, attrs)

	def handle_endtag(self, tag):

		print '%sclose tag: %r' % ('\t'*self.level, tag)

		self.level -= 1

	def handle_data(self, data):

		print '%sdata: %r' %('\t'*(self.level+1), data)





import mechanize

def show_site(url):

	br = mechanize.Browser()

	r = br.open(url)

	print r.info()

	_a = TMP()

	_a.feed(r.read())

	#return _a.links





a = filter(None, show_site(raw_input('url? ')))
