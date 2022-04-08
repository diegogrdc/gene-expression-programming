from Chromosome import Chromosome
import numpy as np


class FitnessEvaluator:
    # We initialize the fitness evaluator
    # TODO: Add correct parameters
    # Params
    # - Fitness cases
    # - Fitness function
    def __init__(self):
        pass

    # Function to evaluate the fitness of a specific population
    # Return values obtained in a list
    def evaluatePopulationFitness(self, population):
        fitness = []
        for ind in population:
            fitness.append(self.evaluateChromosomeFitness(ind))
        return fitness

    def evaluateChromosomeFitness(self, population):
        # TODO: Implement fitness evaluation
        # For now we just return a random number between 0 and 1
        return np.random.random()
