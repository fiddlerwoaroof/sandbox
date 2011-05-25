import functools



class Namespace(object):

    def __init__(self):

        self.__insts = {}

    def _bind_class(self, name, bases, dict):

        cls = type(name, bases, dict)

        cls.__ns = self

        def __init__(slf, *args, **kwargs):

            self.__insts[id(slf)] = slf

            cls.__init__(*args, **kwargs)

        print cls.__init__

        cls.__init__ = __init__

        return cls

    def __call__(self, func):

        result = func

        if not func.__name__.startswith('_'):

            setattr(self, func.__name__, func)

            result = None

        return result

    def __getattribute__(self, name):

        result = object.__getattribute__(self, name)

        if callable(result):

            result=functools.partial(result, self.__inst)

        return result

                



                



class NamespacedClass(object):

    a = Namespace()

    __metaclass__ = a._bind_class

    @a

    def b(self, test_arg):

        print self, test_arg

    
