[htmlentitydefs.name2codepoint.get(y,y) for y in [x[1] or x[2] for x in re.findall('(&([^;]+);|([^&]))', a)]]
result = []
for x in _:
    if isinstance(x, int): result.append(chr(x))
    else: result.append(x)


''.join(result)
htmlentitydefs.codepoint2name[ord('&')]