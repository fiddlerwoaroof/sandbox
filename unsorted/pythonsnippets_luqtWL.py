def a():
	b = [1]
	def c(): b[0] = 2
	print b[0]
	c()
	print b[0]

a()
