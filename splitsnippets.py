"""
Split a file of python snippets into its constituent snippets, splitting
on lines whose first non-whitespace character is #
"""
import sys
counter = 0
with open(sys.argv[1]) as f:
	buffer = []
	for line in f:
		lline = line.strip()
		line = line.rstrip()
		if set(lline) != set(['#']):
			buffer.append(line)
		else:
			with file('%s_%04d.py' %(f.name.rpartition('.')[0], counter), 'w') as g:
				g.write('\n'.join(buffer))
				buffer = []
				counter += 1

