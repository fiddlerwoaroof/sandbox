# Copyright (c) 2011 Edward Langley
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 
# Neither the name of the project's author nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



def f(h):
  def g(n):
     if n <= 1: return 1
     else: return n*h(n-1)

#def e(h):
#  def

def Y(f):
  def g(h):
    def i(x):
      return f(h(h))(x)
    return i
  return g(g)


@Y
def fib(f):
    def _inner(n):
        if n in range(2): return 1
        else: return f(n-1) + f(n-2)
    return _inner


import functools

def bounce(func):
  @functools.wraps(func)
  def _inner(arg):
    result = func(arg)
    return result(fact)
  return _inner

class return_if(object):
    def __init__(self, map):
        self._map = dict(
            (tuple(k) if hasattr(k, '__iter__') else (k,),v) for k,v in map.iteritems()
        )
        self._func = lambda x:x
    def _inner(self, *args):
        if args in self._map: return self._map[args]
        else: return self._func(*args)
    def __call__(self, func):
        self._func = func
        return self._inner
@bounce
@return_if({1: lambda _:1})
def fact(n):
    return lambda x: n*x(n-1)
