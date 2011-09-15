import sys
import lxml.etree
def do():
	xslfile = sys.argv[1]
	xsl = lxml.etree.parse(xslfile)
	xml = lxml.etree.parse('/Users/edwlan/Downloads/google-reader-subscriptions.xml')
	result = xml.xslt(xsl)
	print result
	return result
