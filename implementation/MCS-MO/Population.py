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
    # gene_cnt = Number of ADF genes of each individual
    # class cnt = Number of Homeotic genes of each individual
    # head_sz = Head size of each gene
    # Function_set = functions used on gene expression
    # terminal_set = terminals used on gene expression
    def __init__(self, generations_cnt, population_sz, gene_cnt, class_cnt, head_sz, function_set, terminal_set_sz):
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
        self.t = self.getTailSize()

        # We generate initial population
        self.population = []
        for _ in range(0, self.pop_sz):
            self.population.append(Chromosome(
                self.h, self.t, self.g, self.c, len(self.fn_set), self.tm_set_sz))

    def getTailSize(self):
        return max(list(map(lambda fn: fn.__code__.co_argcount, self.fn_set)))
