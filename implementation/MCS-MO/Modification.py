# This class takes care of modification for genes
# It stores parameters for each modification
# as a rate on how often it will happen
# And implements modifications itself

class Modification:
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

    # TODO: Implement modifications

    # Following we have setters for each mutation rate
    # This gives the option to tweak each value as needed

    # TODO: IMPLEMENT SETTERS
