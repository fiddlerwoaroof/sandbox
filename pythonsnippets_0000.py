## pretty print dict

from emen2.subsystems import routing

for x in sorted(dct):

    print x.ljust(20), '=', dct[x]
