import random

def a(): return random.random()

def b(rando=random): return rando.random()

def c(rando=random.random): return rando()
