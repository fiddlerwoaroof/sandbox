import functools
import collections
def instantiate(cls): return cls()

class Namespace(object):
    def registry(name, bases, dict_):
        cls = type(name, bases, dict_)
        cls.__dict = {}
        return cls
    __metaclass__ = registry
    def __init__(self, instance=None):
        self.__dict__ = self.__dict
        self.__inst = instance
        self._init()
    def _init(self): pass
    def __get__(self, instance, owner):
        result = type(self)(instance)
        return result
    def __check_inst(self):
        if self.__inst is None:
            raise AttributeError, 'this class is unbound, can\'t call methods'
    def __getattribute__(self, name):
        if not name.startswith('_'):
            self.__check_inst()
        result = object.__getattribute__(self, name)
        if callable(result) and not name.startswith('_'):
            result = functools.partial(result, self.__inst)
        return result



class DB(object):
    @instantiate
    class record(Namespace):
        @classmethod
        def _init(self):
            self.__value = 1
        def get(self, db):
            return self.__value
        def set(self, db, value):
            self.__value = value
        def checkparam(self, db):
            print db.param.get()
            return db.param.get() == self.get()
    @instantiate
    class param(Namespace):
        @classmethod
        def _init(self):
            self.__value = 1
        def get(self, db):
            db.othermethod(self.__value)
            return self.__value
        def set(self, db, value):
            db.othermethod(self.__value)
            self.__value = value
            db.othermethod(self.__value)
    def othermethod(self, value): print self, value
    def recordget(self): return self.record.get()
    def recordset(self, value): return self.record.set(value)