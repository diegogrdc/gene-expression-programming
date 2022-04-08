from Chromosome import Chromosome
# Population class representas all chromosomes on each generation.
# It starts with a random generation of chromosomes, and it evaluates their fitness
# and starts evolving through chromosome mutation and fitness, looking to get the best
# evaluation fitness chromosomes at the end
# Remember population uses elitism, and roulette to choose parents in mutation


class Population:
    # Initialize a population with all its relevant information
    # generations_cnt = Number of generations that population will evolve
    # population_sz = Number of individuals on each generation
    def __init__(self, generations_cnt, population_sz, gene_cnt, class_cnt, head_sz, function_set, terminal_set):
        # We store number of generations that we will evolve our chromosomes
        self.generations = generations_cnt
        # We store population size
        self.pop_sz = population_sz
        self.h = head_sz
        self.c = class_cnt
        self.g = gene_cnt
        self.fn_set = function_set
        self.tm_set = terminal_set
        self.t = self.getTailSize()

        # We generate initial population
        self.population = []
        for _ in range(0, self.pop_sz):
            self.population.append(Chromosome(
                self.h, self.t, self.g, self.c, len(self.fn_set), len(self.tm_set)))

    def getTailSize(self):
        return max(list(map(lambda fn: fn.__code__.co_argcount, self.fn_set)))
