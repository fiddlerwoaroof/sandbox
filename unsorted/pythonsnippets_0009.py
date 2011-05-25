from itertools import*;import sys;j=str.join;c=sys.stdin.read();print j('\n',map(lambda b:j(' ',[b,j('',islice(repeat('*'),len(filter(lambda x:x==b,c))))]),map(chr,range(97,122))))

from itertools import*;import sys;j=str.join;c=sys.stdin.read();print j('\n',[j(' ',[b,j('',islice(repeat('*'),len([x for x in c if x==b])))])for b in map(chr,range(97,122))])

import sys;j=str.join;c=sys.stdin.read();print j('\n',[j(' ',[b,j('','*'*c.count(b))])for b in map(chr,range(65,123))])

module Main where import Data.Char;main=getContents>>=(\b->putStrLn$(map chr[65..122]>>=(\c->c:' ':(take(length$filter(\x->x==c)b)$repeat '*')++"\n")))
