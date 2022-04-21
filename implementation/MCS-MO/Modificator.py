import numpy as np
# This class takes care of modification for genes
# It stores parameters for each modification
# as a rate on how often it will happen
# And implements modifications itself


class Modificator:
    # Initialize modification class
    # The idea is to set all params as a default, and then use
    # set functions for special tweaks as needed
    def __init__(self):
        self.mutation_rate = 0.044
        self.inversion_rate = 0.1
        self.IS_transposition_rate = 0.1
        self.RIS_transposition_rate = 0.1
        self.one_point_recombination_rate = 0.3
        self.two_point_recombination_rate = 0.3
        self.gene_recombination_rate = 0.3
        self.gene_transposition_rate = 0.1
        self.homeotic_mutation_rate = 0.044
        self.homeotic_inversion_rate = 0.1
        self.homeotic_IS_transposition_rate = 0.1
        self.homeotic_RIS_transposition_rate = 0.1

    # Apply all modifications to the gene
    # it recieves as a parameter
    # - gene = Gene we will modify
    def modify(self, gene):
        print("Modifying gene", gene)
        self.mutation(gene)
        self.inversion(gene)
        self.ISTransposition(gene)
        self.RISTransposition(gene)
        self.onePointRecombination(gene)
        self.twoPointRecombinatio(gene)
        self.gene_recombination(gene)
        self.gene_transposition(gene)
        self.homeoticMutation(gene)
        self.homeoticInversion(gene)
        self.homeoticISTransposition(gene)
        self.homeoticRISTransposition(gene)

    # TODO: Implement modifications

    # Mutation implementation
    # Just works on ADF genes
    def mutation(self, gene):
        # For each ADF gene
        for ind in gene.adfs:
            # We check all positions
            for i in range(0, len(ind)):
                # If random passes
                if np.random.rand() < self.mutation_rate:
                    # If in head we can do functions
                    if i < gene.h:
                        ind[i] = gene.getRandTerminalOrFunction()
                    # If in tail, just terminals
                    else:
                        ind[i] = gene.getRandTerminal()

    # Inversion implementation
    # Just works on ADF genes
    def inversion(self, gene):
        # If random passes
        if np.random.rand() < self.inversion_rate:
            # Choose random adf, and starting
            # and end point to invert
            # only in the head portion
            idx = np.random.randint(0, gene.g)
            stt = np.random.randint(0, gene.h)
            end = np.random.randint(stt, gene.h)
            # End is exclusive, so we add one
            end = end + 1
            # Invert stt and end in idx gene adf
            gene.adfs[idx][stt:end] = gene.adfs[idx][stt:end][::-1]

    def ISTransposition(self, gene):
        pass

    def RISTransposition(self, gene):
        pass

    def onePointRecombination(self, gene):
        pass

    def twoPointRecombinatio(self, gene):
        pass

    def gene_recombination(self, gene):
        pass

    def gene_transposition(self, gene):
        pass

    def homeoticMutation(self, gene):
        pass

    def homeoticInversion(self, gene):
        pass

    def homeoticISTransposition(self, gene):
        pass

    def homeoticRISTransposition(self, gene):
        pass

    # Following we have setters for each mutation rate
    # This gives the option to tweak each value as needed
    # but keep defaults on init

    # Set Rate of Mutation
    # - rate = new rate

    def setMutationRate(self, rate):
        self.mutation_rate = rate

    # Set Rate of Inversion
    # - rate = new rate
    def setInversionRate(self, rate):
        self.inversion_rate = 0.1

    # Set Rate of IS Transposition
    # - rate = new rate
    def setISTranspositionRate(self, rate):
        self.IS_transposition_rate = 0.1

    # Set Rate of RIS Transposition
    # - rate = new rate
    def setRISTranspositionRate(self, rate):
        self.RIS_transposition_rate = 0.1

    # Set Rate of One Point Recombination
    # - rate = new rate
    def setOnePointRecombinationRate(self, rate):
        self.one_point_recombination_rate = 0.3

    # Set Rate of Two Point Recombination
    # - rate = new rate
    def setTwoPointRecombinationRate(self, rate):
        self.two_point_recombination_rate = 0.3

    # Set Rate of Gene Recombination
    # - rate = new rate
    def setGeneRecombinationRate(self, rate):
        self.gene_recombination_rate = 0.3

    # Set Rate of Gene Transposition
    # - rate = new rate
    def setGeneTranspositionRate(self, rate):
        self.gene_transposition_rate = 0.1

    # Set Rate of Homeotic Mutation
    # - rate = new rate
    def setHomeoticMutationRate(self, rate):
        self.homeotic_mutation_rate = 0.044

    # Set Rate of Homeotic Inversion
    # - rate = new rate
    def setHomeoticInversionRate(self, rate):
        self.homeotic_inversion_rate = 0.1

    # Set Rate of Homeotic IS Transposition
    # - rate = new rate
    def setHomeoticISTranspositionRate(self, rate):
        self.homeotic_IS_transposition_rate = 0.1

    # Set Rate of Homeotic RIS Transposition
    # - rate = new rate
    def setHomeoticRISTranspositionRate(self, rate):
        self.homeotic_RIS_transposition_rate = 0.1
