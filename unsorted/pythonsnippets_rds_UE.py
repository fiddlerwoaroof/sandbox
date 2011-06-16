import code
import StringIO

oraw_input = raw_input
class Tee(object):
	__buffer = StringIO.StringIO()
	@classmethod
	def raw_input(cls, *a, **kw):
		result = oraw_input(*a, **kw)
		print >>cls.__buffer, result
		return result

	def __init__(self, fil_):
		self.fil_ = fil_

	def __getattr__(self, name):
		return getattr(self.fil_, name)

	def read(self, *a):
		result = self.fil_.read(*a)
		print 'hello!!!'
		print >>sys.stdout.fil_, result
		self.__buffer.write(result)
		return result

	def write(self, data):
		self.__buffer.write(data)
		self.fil_.write(data)

	def flush(self):
		self.__buffer.flush()
		self.fil_.flush()

	def get_data(self):
		self.__buffer.seek(0,0)
		return self.__buffer.read()

__builtins__.raw_input = Tee.raw_input
import sys
stdin = sys.stdin = Tee(sys.stdin)
stdout = sys.stdout = Tee(sys.stdout)
stderr = sys.stderr = Tee(sys.stderr)


try:
	a = code.InteractiveConsole()
	a.interact()
except BaseException:
	sys.stderr = sys.stderr.fil_
	raise
else:
	sys.stderr = sys.stderr.fil_
finally:
	sys.stdin = sys.stdin.fil_
	sys.stdout = sys.stdout.fil_
	__builtins__.raw_input = oraw_input

data = stdin.get_data().split('\n')
out = []
counter = 0
for line in data:
	if line.startswith('>>> ') or line.startswith('... '):
		line = line.split(' ', 1)[-1]
		counter += 1
		line = 'l%s = %s' % (counter, line)
	else:
		line = 'repr(l%s) == """%s"""' % (counter, line)
	out.append(line)

print '\n'.join(out)
exec '\n'.join(out)
