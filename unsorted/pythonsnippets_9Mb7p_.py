import itertools
import json

nums = []
with file('num_beings') as f:
  for line in f:
    nums.append(json.loads(line))

with file('test.csv', 'w') as f:
  for list_ in zip(*list(itertools.izip_longest(*nums, fillvalue=0))):
    print >>f, ','.join(str(x) for x in list_)

