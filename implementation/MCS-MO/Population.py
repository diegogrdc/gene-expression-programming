from Chromosome import Chromosome
from Modificator import Modificator
from FitnessEvaluator import FitnessEvaluator
import numpy as np
import copy

# Population class representas all chromosomes on each generation.
# It starts with a random generation of chromosomes, and it evaluates their fitness
# and starts evolving through chromosome mutation and fitness, looking to get the best
# evaluation fitness chromosomes at the end
# Remember population uses elitism, and roulette to choose parents in mutation


class Population:
    # Initialize a population with all its relevant information
    # Params
    # - generations_cnt = Number of generations that population will evolve
    # - population_sz = Number of individuals on each generation
    # - gene_cnt = Number of ADF genes of each individual
    # - class cnt = Number of Homeotic genes of each individual
    # - head_sz = Head size of each gene
    # - Function_set = functions used on gene expression
    # - terminal_set_sz = size of set of terminals used on gene expression. This is fixed for all cases
    # as we need to use the same genes for all cases and we assume same input size
    # - fitness_dir = Directory of fitness cases used
    def __init__(self, generations_cnt, population_sz, gene_cnt, class_cnt, head_sz, function_set, terminal_set_sz, fitness_dir):
        # We store number of generations that we will evolve our chromosomes
        self.generations = generations_cnt
        # We store population size
        self.pop_sz = population_sz
        # We store head size as information
        self.h = head_sz
        # We store class count as information
        self.c = class_cnt
        # We store gene count as information
        self.g = gene_cnt
        # We store function set as information for expression
        self.fn_set = function_set
        # We store terminal set size. When checking fitness, they will be used in order
        # as determined by the fitness evaluator
        self.tm_set_sz = terminal_set_sz
        # We calculate the tail size with the GEP formula
        self.t = self.getTailSize()
        # We store the fitness evaluator
        # aso that logic is taken care by it
        # and population just asks for the data
        self.fitness_eval = FitnessEvaluator(fitness_dir, function_set)

        # We generate initial population
        self.population = []
        for _ in range(0, self.pop_sz):
            self.population.append(Chromosome(
                self.h, self.t, self.g, self.c, len(self.fn_set), self.tm_set_sz))

    # We run the evolutionary process
    # generation by generation
    def run(self):
        # We iterate for each generation
        for _ in range(0, self.generations):
            self.runGeneration()

    # This function contains the run in one generation
    # From evaulation, to selection and modification
    def runGeneration(self):
        # We evaluate the fitness of each individual
        # It is stored in self.fitness list
        # It also creates the fitness roulettes
        self.evalFitness()
        # We create a new empty generation
        new_population = []
        # We keep the best due to elitism
        new_population.append(self.getBestOfGeneration())

        # We need to create another (pop_sz - 1) new chromosomes
        # Remember we choose the parent gene with roulette wheel based on fitness
        # Create a modificator
        modifier = Modificator()
        for _ in range(0, self.pop_sz - 1):
            # We get a parent to replicate from the roulette
            ind = self.getIndividualFromRoulette()
            modifier.modify(ind)

    # This function gets the best individual in a generation
    # based on the calculated fitness

    def getBestOfGeneration(self):
        best_fitness = max(self.fitness)
        best_idx = self.fitness.index(best_fitness)
        return copy.deepcopy(self.population[best_idx])

    # We evaluate fitness for each individual, and keep it stored in
    # self.fitness[] list, so we can use the fitness on the evolutionary process
    # Each time we calculate fitness, we need to obtain a new fitness
    # roulette to choose modifications, so it also calculates and creates this
    # and stores it in self.roulette
    def evalFitness(self):
        self.fitness = self.fitness_eval.evaluatePopulationFitness(
            self.population)
        self.roulette = self.getFitnessRoulette()

    # We generate the fitness roulette
    # Remember after calculating fitness
    # we give bigger slices to bigger fitness
    # so they have a bigger chance on reproduction
    def getFitnessRoulette(self):
        # First we need sum of total fitness
        total = sum(self.fitness)
        # Then, we assign roulette vals as needed
        roulette = []
        act = 0
        for i in range(0, len(self.population)):
            act = act + self.fitness[i]
            roulette.append(act / total)
        return roulette

    def getIndividualFromRoulette(self):
        x = np.random.random()
        for i in range(0, len(self.population)):
            if x < self.roulette[i]:
                return copy.deepcopy(self.population[i])
        return copy.deepcopy(self.population[-1])

    # We calculate the tail size that we need with the formula
    # t = h * (n_max - 1) + 1
    # where n_max is the max number of params used in any function
    def getTailSize(self):
        n_max = max(list(map(lambda fn: fn.__code__.co_argcount, self.fn_set)))
        return self.h * (n_max - 1) + 1
