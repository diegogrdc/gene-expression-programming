import numpy as np
import copy
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
        self.gene_transposition_rate = 0.1
        self.homeotic_mutation_rate = 0.044
        self.homeotic_inversion_rate = 0.1
        self.homeotic_IS_transposition_rate = 0.1
        self.homeotic_RIS_transposition_rate = 0.1

        self.one_point_recombination_rate = 0.8
        self.two_point_recombination_rate = 0.8
        self.gene_recombination_rate = 0.8
        self.homeotic_one_point_recombination_rate = 0.8
        self.homeotic_two_point_recombination_rate = 0.8
        self.homeotic_gene_recombination_rate = 0.8

    # Apply all modifications to the gene
    # Just individual modifications
    # as we need two genes for
    # recombination modifiers
    # it recieves as a parameter
    # - gene = Gene we will modify
    def modify(self, gene):
        self.mutation(gene)
        self.inversion(gene)
        self.ISTransposition(gene)
        self.RISTransposition(gene)
        self.gene_transposition(gene)
        self.homeoticMutation(gene)
        self.homeoticInversion(gene)
        self.homeoticISTransposition(gene)
        self.homeoticRISTransposition(gene)

    # Function used to recombine two genes
    # with the recombination modificatiors we
    # have selected
    # - gene1 = First gene of recombination
    # - gene2 = Second gene of recombination
    # TODO : Implement recombination
    def recombine(self, gene1, gene2):
        self.onePointRecombination(gene1, gene2)
        self.twoPointRecombination(gene1, gene2)
        self.geneRecombination(gene1, gene2)
        self.homeoticOnePointRecombination(gene1, gene2)
        self.homeoticTwoPointRecombination(gene1, gene2)
        self.homeoticGeneRecombination(gene1, gene2)

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
        # If random not passes we return
        if np.random.rand() >= self.inversion_rate:
            return
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

    # Insertion Sequence (IS)
    # Transposition implementation
    # Just works on ADF genes
    def ISTransposition(self, gene):
        # If random not passes we return
        if np.random.rand() >= self.IS_transposition_rate:
            return
        # We pick a random adf
        # start, end
        # and pos to insert
        idx = np.random.randint(0, gene.g)
        stt = np.random.randint(0, gene.sz)
        end = np.random.randint(stt, gene.sz)
        pos = np.random.randint(1, gene.h)
        # End is exclusive, so we add one
        end = end + 1
        # Create new mov sublist
        mov = copy.deepcopy(gene.adfs[idx][stt:end])
        # Add new part to chromosome
        gene.adfs[idx] = gene.adfs[idx][:pos] + mov + gene.adfs[idx][pos:]
        # Delete extra part from head
        head_sz = gene.h + len(mov)
        gene.adfs[idx] = gene.adfs[idx][:gene.h] + gene.adfs[idx][head_sz:]

    # Root Insertion Sequence (RIS)
    # Transposition implementation
    # Just works on ADF genes
    def RISTransposition(self, gene):
        # If random not passes we return
        if np.random.rand() >= self.RIS_transposition_rate:
            return
        # We pick a random adf
        # start, end,
        # making sure start is a function
        idx = np.random.randint(0, gene.g)
        # Choose start and move until a function is found
        stt = np.random.randint(0, gene.h)
        while stt < gene.h and gene.adfs[idx][stt][0] != 'f':
            stt = stt + 1
        # If function was not found, do nothing
        if stt == gene.h:
            return
        end = np.random.randint(stt, gene.sz)
        # End is exclusive, so we add one
        end = end + 1
        # Create new mov sublist
        mov = copy.deepcopy(gene.adfs[idx][stt:end])
        # Add new part to chromosome at beginning
        gene.adfs[idx] = mov + gene.adfs[idx]
        # Delete extra part from head
        head_sz = gene.h + len(mov)
        gene.adfs[idx] = gene.adfs[idx][:gene.h] + gene.adfs[idx][head_sz:]

    # Gene Transposition implementation
    # Just works on ADF genes
    def gene_transposition(self, gene):
        # If random not passes we return
        if np.random.rand() >= self.gene_transposition_rate:
            return
        # Pick a gene to move
        idx = np.random.randint(0, gene.g)
        # Delete it from current place
        mov = gene.adfs.pop(idx)
        # Add at start
        gene.adfs.insert(0, mov)

    # Mutation implementation
    # Just works on Homeotic genes
    def homeoticMutation(self, gene):
        # For each Homeotic gene
        for ind in gene.genes:
            # We check all positions
            for i in range(0, len(ind)):
                # If random passes
                if np.random.rand() < self.homeotic_mutation_rate:
                    # If in head we can do functions
                    if i < gene.h:
                        ind[i] = gene.getRandADFOrFunction()
                    # If in tail, just terminals
                    else:
                        ind[i] = gene.getRandADF()

    # Homeotic Inversion implementation
    # Just works on Homeotic genes
    def homeoticInversion(self, gene):
        # If random not passes we return
        if np.random.rand() >= self.homeotic_inversion_rate:
            return
        # Choose random homeotic, and starting
        # and end point to invert
        # only in the head portion
        idx = np.random.randint(0, gene.c)
        stt = np.random.randint(0, gene.h)
        end = np.random.randint(stt, gene.h)
        # End is exclusive, so we add one
        end = end + 1
        # Invert stt and end in idx gene adf
        gene.genes[idx][stt:end] = gene.genes[idx][stt:end][::-1]

    # Homeotic Insertion Sequence (IS)
    # Transposition implementation
    # Just works on Homeotic genes
    def homeoticISTransposition(self, gene):
        # If random not passes we return
        if np.random.rand() >= self.homeotic_IS_transposition_rate:
            return
        # We pick a random homeotic gene
        # start, end
        # and pos to insert
        idx = np.random.randint(0, gene.c)
        stt = np.random.randint(0, gene.sz)
        end = np.random.randint(stt, gene.sz)
        pos = np.random.randint(1, gene.h)
        # End is exclusive, so we add one
        end = end + 1
        # Create new mov sublist
        mov = copy.deepcopy(gene.genes[idx][stt:end])
        # Add new part to chromosome
        gene.genes[idx] = gene.genes[idx][:pos] + mov + gene.genes[idx][pos:]
        # Delete extra part from head
        head_sz = gene.h + len(mov)
        gene.genes[idx] = gene.genes[idx][:gene.h] + gene.genes[idx][head_sz:]

    # Homeotic Root Insertion Sequence (RIS)
    # Transposition implementation
    # Just works on Homeotic genes
    def homeoticRISTransposition(self, gene):
        # If random not passes we return
        if np.random.rand() >= self.homeotic_RIS_transposition_rate:
            return
        # We pick a random homeotic
        # start, end,
        # making sure start is a function
        idx = np.random.randint(0, gene.c)
        # Choose start and move until a function is found
        stt = np.random.randint(0, gene.h)
        while stt < gene.h and gene.genes[idx][stt][0] != 'f':
            stt = stt + 1
        # If function was not found, do nothing
        if stt == gene.h:
            return
        end = np.random.randint(stt, gene.sz)
        # End is exclusive, so we add one
        end = end + 1
        # Create new mov sublist
        mov = copy.deepcopy(gene.genes[idx][stt:end])
        # Add new part to chromosome at beginning
        gene.genes[idx] = mov + gene.genes[idx]
        # Delete extra part from head
        head_sz = gene.h + len(mov)
        gene.genes[idx] = gene.genes[idx][:gene.h] + gene.genes[idx][head_sz:]

    def onePointRecombination(self, gene1, gene2):
        # If random not passes we return
        if np.random.rand() >= self.one_point_recombination_rate:
            return
        # Choose random adf, and point
        # of recombination
        idx = np.random.randint(0, gene1.g)
        pt = np.random.randint(0, gene1.sz)
        # Recombine
        nwadf1 = gene1.adfs[idx][:pt] + gene2.adfs[idx][pt:]
        nwadf2 = gene2.adfs[idx][:pt] + gene1.adfs[idx][pt:]
        gene1.adfs[idx] = nwadf1
        gene2.adfs[idx] = nwadf2

    def twoPointRecombination(self, gene1, gene2):
        # If random not passes we return
        if np.random.rand() >= self.two_point_recombination_rate:
            return
        # Choose random adf, and two points
        # of recombination
        idx = np.random.randint(0, gene1.g)
        pt1 = np.random.randint(0, gene1.sz - 1)
        pt2 = np.random.randint(pt1, gene1.sz)
        # Recombine
        nwadf1 = gene1.adfs[idx][:pt1] + \
            gene2.adfs[idx][pt1:pt2] + gene1.adfs[idx][pt2:]
        nwadf2 = gene2.adfs[idx][:pt1] + \
            gene1.adfs[idx][pt1:pt2] + gene2.adfs[idx][pt2:]
        gene1.adfs[idx] = nwadf1
        gene2.adfs[idx] = nwadf2

    def geneRecombination(self, gene1, gene2):
        # If random not passes we return
        if np.random.rand() >= self.gene_recombination_rate:
            return
        # Choose random and point
        # of recombination in gene length
        pt = np.random.randint(0, gene1.g)
        pt = 1
        # Recombine
        nwadfs1 = gene1.adfs[:pt] + gene2.adfs[pt:]
        nwadfs2 = gene2.adfs[:pt] + gene1.adfs[pt:]
        gene1.adfs = nwadfs1
        gene2.adfs = nwadfs2

    def homeoticOnePointRecombination(self, gene1, gene2):
        # If random not passes we return
        if np.random.rand() >= self.one_point_recombination_rate:
            return
        # Choose random gene, and point
        # of recombination
        idx = np.random.randint(0, gene1.c)
        pt = np.random.randint(0, gene1.sz)
        # Recombine
        nwgene1 = gene1.genes[idx][:pt] + gene2.genes[idx][pt:]
        nwgene2 = gene2.genes[idx][:pt] + gene1.genes[idx][pt:]
        gene1.genes[idx] = nwgene1
        gene2.genes[idx] = nwgene2

    def homeoticTwoPointRecombination(self, gene1, gene2):
        # If random not passes we return
        if np.random.rand() >= self.two_point_recombination_rate:
            return
        # Choose random gene, and two points
        # of recombination
        idx = np.random.randint(0, gene1.c)
        pt1 = np.random.randint(0, gene1.sz - 1)
        pt2 = np.random.randint(pt1, gene1.sz)
        # Recombine
        nwgene1 = gene1.genes[idx][:pt1] + \
            gene2.genes[idx][pt1:pt2] + gene1.genes[idx][pt2:]
        nwgene2 = gene2.genes[idx][:pt1] + \
            gene1.genes[idx][pt1:pt2] + gene2.genes[idx][pt2:]
        gene1.genes[idx] = nwgene1
        gene2.genes[idx] = nwgene2

    def homeoticGeneRecombination(self, gene1, gene2):
        # If random not passes we return
        if np.random.rand() >= self.gene_recombination_rate:
            return
        # Choose random and point
        # of recombination in gene length
        pt = np.random.randint(0, gene1.c)
        pt = 1
        # Recombine
        nwgenes1 = gene1.genes[:pt] + gene2.genes[pt:]
        nwgenes2 = gene2.genes[:pt] + gene1.genes[pt:]
        gene1.genes = nwgenes1
        gene2.genes = nwgenes2

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
        self.inversion_rate = rate

    # Set Rate of IS Transposition
    # - rate = new rate
    def setISTranspositionRate(self, rate):
        self.IS_transposition_rate = rate

    # Set Rate of RIS Transposition
    # - rate = new rate
    def setRISTranspositionRate(self, rate):
        self.RIS_transposition_rate = rate

    # Set Rate of Gene Transposition
    # - rate = new rate
    def setGeneTranspositionRate(self, rate):
        self.gene_transposition_rate = rate

    # Set Rate of Homeotic Mutation
    # - rate = new rate
    def setHomeoticMutationRate(self, rate):
        self.homeotic_mutation_rate = rate

    # Set Rate of Homeotic Inversion
    # - rate = new rate
    def setHomeoticInversionRate(self, rate):
        self.homeotic_inversion_rate = rate

    # Set Rate of Homeotic IS Transposition
    # - rate = new rate
    def setHomeoticISTranspositionRate(self, rate):
        self.homeotic_IS_transposition_rate = rate

    # Set Rate of Homeotic RIS Transposition
    # - rate = new rate
    def setHomeoticRISTranspositionRate(self, rate):
        self.homeotic_RIS_transposition_rate = rate

    # Set Rate of One Point Recombination
    # - rate = new rate
    def setOnePointRecombinationRate(self, rate):
        self.one_point_recombination_rate = rate

    # Set Rate of Two Point Recombination
    # - rate = new rate
    def setTwoPointRecombinationRate(self, rate):
        self.two_point_recombination_rate = rate

    # Set Rate of Gene Recombination
    # - rate = new rate
    def setGeneRecombinationRate(self, rate):
        self.gene_recombination_rate = rate

    # Set Rate of Homeotic One Point Recombination
    # - rate = new rate
    def setHomeoticOnePointRecombinationRate(self, rate):
        self.homeotic_one_point_recombination_rate = rate

    # Set Rate of Homeotic Two Point Recombination
    # - rate = new rate
    def setHomeoticTwoPointRecombinationRate(self, rate):
        self.homeotic_two_point_recombination_rate = rate

    # Set Rate of Homeotic Gene Recombination
    # - rate = new rate
    def setHomeoticGeneRecombinationRate(self, rate):
        self.homeotic_gene_recombination_rate = rate
