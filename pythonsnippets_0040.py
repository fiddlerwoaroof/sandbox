import abc

class Pipe(object):

    __metaclass__ = abc.ABCMeta

    @property

    def file(self): return self.__file

    def __init__(self, file, *args, **kw):

        self.__file = file

        self.__delim = '\n'

        self.init(*args, **kw)

    def init(self, *args, **kw): pass
