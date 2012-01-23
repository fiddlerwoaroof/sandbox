# Copyright (c) 2011 Edward Langley
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# Neither the name of the project's author nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import collections

class dkeydict(collections.Mapping):
	def __init__(self, items=None):
		#: caching only
		self.dict = {}

		items = items or []
		self.list = items.items() if hasattr(items, 'items') else items
	def __iter__(self): return iter(self.list)
	def __len__(self): return len(self.list)

	def __getitem__(self, key):
		result = []

		#: which item to get
		count = 0
		counter = 0

		#: how many?
		num = 1

		#: which ones to get?
		skip = 0
		idx = 0

		if isinstance(key, tuple) and 1 < len(key) < 5:
			if len(key) == 2:
				key, count = key
			elif len(key) == 3:
				key, count, num = key
			else:
				key, count, num, skip = key

			capturing = False
			for k,v in reversed(self.list):
				if k == key:
					if len(result) == num: break

					if counter >= count: capturing = True
					counter += 1

					if idx != skip:
						capturing = False
						idx += 1
					else:
						capturing = True
						idx = 0

					if capturing: result.append(v)



		elif isinstance(key, slice):
			return self.list[slice]
		else:
			if key in self.dict: return self.dict[key]
			else:
				result = reversed([v for k,v in self.list if k == key]).next()
				self.dict[key] = result

		return result

