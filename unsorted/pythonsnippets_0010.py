def mdir1(n):
    print '\n'.join((lambda l: ['\t'.join([a.ljust(25) for a in x]) for x in zip(l[0::3],l[1::3],l[2::3])])(sorted(dir(n) if n!=None else dir())))