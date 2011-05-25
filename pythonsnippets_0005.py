class test(HTMLParser.HTMLParser):
    intable = False
    titling = False
    capturing = True
    cdata = []
    out = u''
    def handle_starttag(self, tag, attrs):
        print tag,attrs
        if dict(attrs).get('class', None) == 'm': self.capturing = False
        if tag.lower() == 'table': self.intable = True
        elif tag.lower() == 'title': self.titling = True
        elif tag.lower() == 'td' and dict(attrs).get('class', None) != 'm':
            self.capturing = True
    def handle_endtag(self, tag):
        if self.titling and tag.lower() == 'title': self.titling=False
        if self.capturing:
            out = u'\n'.join(self.cdata)
            self.cdata = []
            self.out += '\n' + out
            #print out
    def handle_data(self, data):
        if self.capturing and self.intable and data.strip() != '': self.cdata.append(data.decode('utf-8'))
        if self.titling: self.cdata.append(u'HEADING: %s' % data.decode('utf-8'))


b=test()
for x in range(1,14):
    with file('3_%02d.html' % x, 'rU') as a: (b.reset(),setattr(b, 'capturing', True), b.feed(a.read()))
a = file('2_01.html')
b.feed(a.read())