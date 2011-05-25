a = {
    0: set([1, 14, 16, 17, 19, 20, 21, 22]),
    1: set([2]),
    2: set([]),
    14: set([15]),
    15: set([]),
    16: set([18]),
    17: set([]),
    18: set([]),
    19: set([]),
    20: set([]),
    21: set([]),
    22: set([])
}
def lookup(lis, table):
    cset = table[lis.pop(0)]
    ckey = None
    for x in lis[:-1]:
        if x in cset:
            ckey = x
            cset = table[x]
            print x, cset
        else:
            raise Exception()
    if lis[-1] in cset:
        key = lis[-1]
        return key, table[key]
    else:
        raise Exception()

import UserDict
import operator
class Tree(object, UserDict.DictMixin):
    def __init__(self, table, root):
        self.key = root
        self.filled = False
        self.children = {}
        if root in table:
            result = []
            for child in table[root]:
                result.append((child, Tree(table, child)))
            self.filled = True
            self.children.update(result)

    def __getitem__(self, key):
        if hasattr(key, '__iter__'):
            return self.find([self.key] + list(key))
        return self.children[key]
    def keys(self):
        return self.children.keys()
    def find(self, path):
        if len(path) == 1:
            return self
        else:
            value = self[path[1]]
            if value is not None:
                value = value.find(path[1:])
                return value
    def __str__(self):
        return '\n'.join(self.mkstrtree(0))
    def mkstrtree(self, level, space='--'):
        result = [space*level+str(level+1)+space+str(self.key)]
        for id, child in self.children.items():
            result.extend(child.mkstrtree(level+1))
        return result
    def mktree(self):
        result = {}
        def setitem(dict, key, value): dict[key] = value
        for key, value in self.children.items():
            if value.filled:
                setitem(result, key, value.mktree())
            else:
                setitem(result, key, None)
        return result
    def count(self):
        return len(self) + reduce(operator.add,
                                  [x.count() for x in self.children.values()],
                                  0)


b = Tree(a, 135);print b