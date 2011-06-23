import string


class Test(string.Formatter):
	def get_field(self, field_name, args, kwargs):
		#result = string.Formatter.get_field(self, field_name, args, kwargs)
		result = ('a','a')
		print 'get_field(',self, field_name, args, kwargs,'):', result
		return result
	def get_value(self, key, args, kwargs):
		print 'get_value(',self, key, args, kwargs,')'
		return "asd"
