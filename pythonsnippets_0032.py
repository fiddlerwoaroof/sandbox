import re

re.sub('&([^;]+);', r'&.\1.;', 'sdsfjsdlflsdfsdf&asdasd;dfsdfgsfdgfsd&dsfdsaf; &sfgfdgds;')

import htmlentitydefs

result = []

for x in a:

    n = htmlentitydefs.codepoint2name.get(ord(x))

    if n is not None: x = '&%s;' % n

    result.append(x)
