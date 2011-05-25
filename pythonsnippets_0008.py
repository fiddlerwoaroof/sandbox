def mdir(name=None):

    if name != None:

        lis = dir(name);

    else:

        lis = dir()

    lis.sort();

    lis = zip(lis[0::3],lis[1::3],lis[2::3])

    in_ = lambda x: [a.ljust(25) for a in x]

    out = lambda lis: ['\t'.join(in_(x)) for x in lis]

    print '\n'.join(out(lis))
