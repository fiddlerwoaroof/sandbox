from twisted.spread import pb

from twisted.internet import reactor

from twisted.python import util



factory = pb.PBClientFactory()

reactor.connectTCP("localhost", 8789, factory)

d = factory.getRootObject()

a = []

d.addCallback(lambda object: object.callRemote("nextQuote"))

d.addCallback(lambda echo: a.append(echo))

d.addErrback(lambda reason: 'error: '+str(reason.value))

d.addCallback(util.println)

reactor.run()
