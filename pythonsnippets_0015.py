from twisted.spread import pb
from twisted.internet import reactor

def main():
foo = Foo()
factory = pb.PBClientFactory()
reactor.connectTCP("localhost", 8800, factory)
factory.getRootObject().addCallback(foo.step1)
reactor.run()


class Foo:
def __init__(self):
self.oneRef = None
def step1(self, obj):
print "got one object:", obj
self.oneRef = obj
print "asking it to getTwo"
self.oneRef.callRemote("getTwo").addCallback(self.step2)
def step2(self, two):
print "got two object:", two
print "giving it back to one"
print "one is", self.oneRef
self.oneRef.callRemote("checkTwo", two)


main()