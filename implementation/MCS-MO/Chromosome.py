import numpy as np

# Chromosome is a representation of a genotype
# Specifically in this implementation, it represents a
# Multi Cellular System with Multiple Output (MCS-MO)
# On this class we keep the cellular information
# The expression (evaluation) of these chromosomes is not part of this class
# Evaluation should be done somewhere else, as this class has no
# knoledge of functions or terminal meaning
# Population will keep function and terminal logic, as it is the same for all genes in an experiment
# and it is unnecesary to have functions and terminals stored on each chromosome


class Chromosome:
    # Initialization of information of the gene
    # Params:
    # - head_sz = Nnumber of positions used in the head portion of a gene
    # - tail_sz = Number of positions used in the tail portion of a gene
    # - gene_cnt = Number of ADF genes the chromosome will contain
    # - class_cnt = Number of homeotic genes the chromosome will contain
    # - function_count = Number of functions available for this chromosome
    # - terminal_count = Number of terminals available for this chromosome
    def __init__(self, head_sz, tail_sz, gene_cnt, class_cnt, function_count, terminal_count):
        # Head size is usually known as h
        self.h = head_sz
        # Tail size is usually known as t
        self.t = tail_sz
        # As a Multicellular chromosome, it has multiple genes that will work as ADFs
        self.g = gene_cnt
        # As a Multicellular chromosome, it has multiple genes
        self.c = class_cnt
        # We need to store function count to generate the chromosome (f0, f1, f2, f3, etc)
        # The functions will be stored in Population, as they are the same for all chromosomes and not needed here
        self.fn_cnt = function_count
        # We need to store terminal count to generate the chromosome (t0, t1, t2, t3, etc)
        self.tm_cnt = terminal_count

        # We generate an initial random Chromosome
        # First we generate the regular ADF genes
        # We will store each ADF gene as a string list element
        self.adfs = []
        for _ in range(0, self.g):
            self.adfs.append(self.getRandomADFGene())
        # Then we generate the homeotic genes, one for each class
        # We store them as a string list element
        self.genes = []
        for _ in range(0, self.c):
            self.genes.append(self.getRandomHomeoticGene())

    # Function used to generate a random ADF gene after initialization
    def getRandomADFGene(self):
        gene = []
        # Generate head part of gene
        # Head can have both functions and terminals with equal probability
        for i in range(0, self.h):
            gene.append(
                (self.getRandTerminal() if np.random.random()
                 < 0.5 else self.getRandFunction()))
        # Tail can have only terminals
        for i in range(0, self.t):
            gene.append(self.getRandTerminal())
        return gene

    # Function used to generate a random Homeotic gene after initialization
    def getRandomHomeoticGene(self):
        gene = []
        # Generate head part of gene
        # Head can have both functions and terminals with equal probability
        for i in range(0, self.h):
            gene.append(
                (self.getRandADF() if np.random.random()
                 < 0.5 else self.getRandFunction()))
        # Tail can have only terminals
        for i in range(0, self.t):
            gene.append(self.getRandADF())
        return gene

    # Function used to get a random terminal for an ADF gene
    def getRandTerminal(self):
        return ("t", np.random.randint(0, self.tm_cnt))

    # Function used to get a random function for any type of gene
    def getRandFunction(self):
        return ("f", np.random.randint(0, self.fn_cnt))

    # Function used to get a random ADF for a Homeotic gene
    def getRandADF(self):
        return ("a", np.random.randint(0, self.g))

    def printChromosome(self):
        print(self.adfs)
        print(self.genes)

    def __str__(self):
        return "\n    GENES: {}\n    ADFS:{}".format(self.genes, self.adfs)
