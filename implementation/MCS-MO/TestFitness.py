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


def test():
    function_set = [add, sub, mul, div]
    fitness = FitnessEvaluator('./../training/', function_set)
    fitness.evaluatePopulationFitness(['p1', 'p2', 'p3', 'p4', 'p5'])


test()
