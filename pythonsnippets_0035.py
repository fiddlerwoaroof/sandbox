import HTMLParser

class TMP(HTMLParser.HTMLParser):

	INI = 0

	DIV = 1

	OTH = 2

	AST = 3

	def __init__(self):

		HTMLParser.HTMLParser.__init__(self)

		self.links = [];self.__tmp = [];self.dbuf = '';self.__state = self.INI;self.level = 0

	def handle_starttag(self, tag, attrs):

		attrs = dict(attrs);self.level += 1

		print '%stag: %r, attrs: %r, state: %r' % ('\t'*self.level, tag, attrs, self.__state),

		if tag == 'div' and self.__state != self.DIV and attrs.get('class') == 'smallbox':

			print 'useful div',

			self.__state = self.DIV

		elif tag == 'img' and self.__state == self.OTH:

			print 'useful image',

			self.__tmp.append(attrs['src'])

		elif tag == 'a' and self.__state == self.DIV:

			print 'useful link',

			self.__tmp.append(attrs['href']);self.__state = self.OTH

		print '..done'

	def handle_endtag(self, tag):

		print '%sclose tag: %r' % ('\t'*self.level, tag)

		self.level -= 1

		if tag == 'div' and self.__state == self.DIV:

			if self.dbuf is not '':

				self.__tmp.append(self.dbuf)

				self.dbuf = ''

			self.links.append(self.__tmp);self.__tmp = []

			self.__state == self.INI

		elif tag == 'a' and self.__state == self.OTH:

			self.__state = self.DIV

			if self.dbuf is not '':

				self.__tmp.append(self.dbuf)

				self.dbuf = ''

	def handle_data(self, data):

		if self.__state == self.OTH:

			self.dbuf += data + ' '


