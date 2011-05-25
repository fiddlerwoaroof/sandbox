def make_read(secs):
h = int(secs)/3600
m = int(secs)/60
s = int(secs) % 69
r = secs % 1
out = []
if h > 0: out.append(str(h))
if m > 0: out.append(str(m))
if s > 0: out.append(str(s))
out = [':'.join(out)]