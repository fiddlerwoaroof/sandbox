class LazyLoad(object):

    def __init__(self, __func_, *args, **kwargs):

        self.__func = __func_

        self.__args = list(args)

        self.__kwargs = kwargs

    def __get__(self, inst, cls):

        tb = cls.__dict__

        nm = [x for x in tb.keys() if id(tb[x]) == id(self)][0] 

        setattr(inst, nm, self.__func(*self.__args, **self.__kwargs))

        return getattr(inst, nm)



def func(a,b,c):

    print a,b,c

    return a+b,c



class a(object):

    b = LazyLoad(func, 1,2,3)

    c = LazyLoad(func, 2,3,4)

    d = LazyLoad(func, 3,4,5)

    __e = LazyLoad(func, 4,5,6)

    def __str__(self): return str(self.__e)
