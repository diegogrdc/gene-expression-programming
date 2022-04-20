from Chromosome import Chromosome
import numpy as np
import os
import re


class FitnessEvaluator:
    # We initialize the fitness evaluator
    # TODO: Add correct parameters
    # Params
    # - dir_cases = Directory Where we will find our fitness cases
    # - Fitness function
    def __init__(self, dir_cases):
        self.dir = dir_cases
        # We extract all the cases from the directory, and store them
        self.initCases()
        pass

    # With directory name, we store all our fitness cases
    def initCases(self):
        # Iterate over every file in our directory
        self.test_names = []
        self.test_n = []
        self.test_c = []
        self.test_objs = []
        for filename in os.listdir(self.dir):
            # Store test name
            self.test_names.append(filename)
            # Get test contents
            file = open(self.dir + filename, 'r')
            content = file.read()
            nums = re.findall(r'\d+', content)
            nums = list(map(int, nums))
            self.test_n.append(nums[0])
            self.test_c.append(nums[1])
            self.test_objs.append(nums[2:])
            # assert(nums[0] == len(nums[2:]))
            print(filename)
            print(nums[0] == len(nums[2:]))

            print(nums[0], nums[1])
            print(nums[2:])

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
