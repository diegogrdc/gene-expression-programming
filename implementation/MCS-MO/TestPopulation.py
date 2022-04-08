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
    return x / y


def test():
    fitness_eval = FitnessEvaluator()
    function_set = [add, sub, mul, div]
    terminal_set = ['a', 'b', 'c', 'd', 'e']
    pop = Population(10, 10, 3, 3, 5, function_set,
                     len(terminal_set), fitness_eval)
    for i, chrom in enumerate(pop.population):
        print("Individual #", i)
        chrom.printChromosome()
        print("")

    pop.run()


test()
