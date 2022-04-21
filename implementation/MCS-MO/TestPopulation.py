import math
from Population import Population
from Chromosome import Chromosome
from FitnessEvaluator import FitnessEvaluator


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return 0
    return x / y


def sqrt(x):
    if x < 0:
        return 0
    return math.sqrt(x)


def test():
    function_set = [add, sub, mul, div, sqrt]
    terminal_set = ['a', 'b', 'c', 'd', 'e']
    pop = Population(2, 2, 3, 4, 5, function_set,
                     len(terminal_set), './../training/')
    for i, chrom in enumerate(pop.population):
        print("Individual #", i)
        chrom.printChromosome()
        print("")

    pop.run()


test()
