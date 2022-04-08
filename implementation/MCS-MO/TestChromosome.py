import math
from Chromosome import Chromosome


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def sqrt(x):
    return math.sqrt(x)


def test():
    h_sz = 4
    t_sz = h_sz * (2 - 1) + 1
    ch = Chromosome(h_sz, t_sz, 3, 3, 3, 5)
    print(ch.adfs)
    print(ch.genes)


test()
