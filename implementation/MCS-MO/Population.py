from Chromosome import Chromosome
from Modificator import Modificator
from FitnessEvaluator import FitnessEvaluator
import matplotlib.pyplot as plt
import numpy as np
import copy
import pickle

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
    # - testing_dir = Directory of test cases used
    def __init__(self, generations_cnt, population_sz, gene_cnt, class_cnt, head_sz, function_set, terminal_set_sz, fitness_dir, testing_dir, pickle_flag):
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
        self.fitness_eval = FitnessEvaluator(
            fitness_dir, testing_dir, function_set)

        # We generate initial population
        self.population = []
        for _ in range(0, self.pop_sz):
            self.population.append(Chromosome(
                self.h, self.t, self.g, self.c, len(self.fn_set), self.tm_set_sz))
        # Check if stored, then we replace random
        # population with this one
        if pickle_flag == True:
            self.checkPickle()

        # Init history list
        self.best_hist = []

    def checkPickle(self):
        infile = open('best_store.txt', 'rb')
        new_pop = pickle.load(infile)
        infile.close()
        self.population = new_pop

    # We run the evolutionary process
    # generation by generation
    def run(self):
        # We iterate for each generation
        for i in range(0, self.generations):
            self.runGeneration()
            self.testGeneration()
            if i % 1000 == 0 and i > 0:
                self.plotHist()
                pass

    def plotHist(self):
        plt.plot(range(0, len(self.best_hist)),
                 self.best_hist, color='red')
        plt.xlabel('iteraciones')
        plt.ylabel('mejor encontrado')
        plt.title('Mejores en evolucion')
        plt.show()

   # After every iteration, we test and
   # save the results of the best of generation
    def testGeneration(self):
        best = self.getBestOfGeneration()
        waste = self.fitness_eval.evaluateChromosomeFitness(
            best, 0, False, None)
        self.fitness_eval.writeTestResult(best, waste, 21)

    # This function contains the run in one generation
    # From evaulation, to selection and modification
    def runGeneration(self):
        # We evaluate the fitness of each individual
        # It is stored in self.fitness list
        # It also creates the fitness roulettes
        self.evalFitness()
        # We create a new empty generation
        new_population = []

        # Create a modificator
        modifier = Modificator()
        # We need to create another (pop_sz - 1) new chromosomes
        # We make tourney and recombine genes
        # before pushing to new gen
        while len(new_population) < self.pop_sz - 1:
            # We get a parent to replicate from the roulette
            ind1 = self.getIndividualFromTournament()
            ind2 = self.getIndividualFromTournament()
            # Recombine both genes
            modifier.recombine(ind1, ind2)
            # We modify the individual before adding to new population
            modifier.modify(ind1)
            modifier.modify(ind2)
            new_population.append(ind1)
            if len(new_population) < self.pop_sz - 1:
                new_population.append(ind2)

        # At last
        # We keep the best due to elitism
        new_population.append(self.getBestOfGeneration())
        # Store best so we can graph it
        self.best_hist.append(max(self.fitness))

        # Assign our modified population
        self.population = new_population

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
            self.population, True)

    # NOT USED AS WE MOVED TO TOURNAMENT
    # We generate the fitness roulette
    # Remember after calculating fitness
    # we give bigger slices to bigger fitness
    # so they have a bigger chance on reproduction
    def getFitnessRoulette(self):
        # First we need sum of total fitness
        total = sum(self.fitness) * len(self.fitness)
        # Then, we assign roulette vals as needed
        roulette = []
        act = 0
        for i in range(0, len(self.population)):
            act = act + self.fitness[i]
            roulette.append(act / total)
        return roulette

    # Function that randomly chooses k
    # different individuals and returns the best
    # one of them to continue evolution
    def getIndividualFromTournament(self, k=3):
        inds = []
        fits = []
        for _ in range(0, k):
            idx = np.random.randint(0, self.pop_sz)
            inds.append(copy.deepcopy(self.population[idx]))
            fits.append(self.fitness[idx])
        winner_idx = np.argmax(fits)
        return inds[winner_idx]

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
