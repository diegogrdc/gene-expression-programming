from Chromosome import Chromosome
from GeneExpressor import GeneExpressor
import numpy as np
import os
import re


class FitnessEvaluator:
    # We initialize the fitness evaluator
    # TODO: Add correct parameters
    # Params
    # - dir_cases = Directory Where we will find our fitness cases
    def __init__(self, dir_cases, function_set):
        self.dir = dir_cases
        # We extract all the cases from the directory, and store them
        self.initCases()
        # Set up gene expression class to deal with
        # gene expression when needed
        # We store function set there
        self.gene_expressor = GeneExpressor(function_set)

        # We setup our heuristics
        # This is problem specific
        # In this case we have four
        self.heuristics = [self.heuristic_next_fit, self.heuristic_first_fit,
                           self.heuristic_best_fit, self.heuristic_worst_fit]

    # Following we have the 4 heuristics used
    # Each recieves
    # - terminals = The terminals that represent
    # the current state of the problem
    # They update thee problem as needed

    # Remember structure of terminals in a 24 size array
    # [N, C, # of bins, curr obj, 20 possible bins]

    # Consider current bin. If object fits, insert, else
    # add a new bin and insert
    def heuristic_next_fit(self, terminals):
        # Get last bin
        # + 4 to adjust as we have 4 nums unrelated before
        # - 1 to index in zero
        bin = terminals[2] - 1 + 4
        c = terminals[1]
        nw = terminals[3]
        # If new item fits we just add it in same bin
        if terminals[bin] + nw <= c:
            terminals[bin] = terminals[bin] + nw
        # Else we create new bin and add it there
        else:
            terminals[2] = terminals[2] + 1
            terminals[bin + 1] = nw

    # Consider all bins, and  find first fit
    # If did not find any, add a new bin and insert
    def heuristic_first_fit(self, terminals):
        c = terminals[1]
        nw = terminals[3]
        bin = terminals[2] - 1 + 4
        # Search bins left to right
        for i in range(4, len(terminals)):
            # If it fits, we store and return
            if terminals[i] + nw <= c:
                terminals[i] = terminals[i] + nw
                # Check if new bin
                if i > bin:
                    terminals[2] = terminals[2] + 1
                return
        # We should never arrive here, as we should always find a place to store
        assert(0 == 1)

    # Consider all bins, and  find best fit
    # best means one with least residue left
    # If did not find any, add a new bin and insert
    def heuristic_best_fit(self, terminals):
        c = terminals[1]
        nw = terminals[3]
        bin = terminals[2] - 1 + 4
        bst = -1
        bst_fit = c + 1
        for i in range(4, len(terminals)):
            if terminals[i] + nw <= c and c - nw - terminals[i] < bst_fit:
                bst_fit = c - nw - terminals[i]
                bst = i
        if bst > bin:
            terminals[2] = terminals[2] + 1
        terminals[bst] = terminals[bst] + nw

    # Consider all bins, and  find worst fit
    # worst means one with most residue left
    # If did not find any, add a new bin and insert
    def heuristic_worst_fit(self, terminals):
        c = terminals[1]
        nw = terminals[3]
        bin = terminals[2] - 1 + 4
        wst = -1
        wst_fit = -1
        for i in range(4, bin + 1):
            if terminals[i] + nw <= c and c - nw - terminals[i] > wst_fit:
                wst_fit = c - nw - terminals[i]
                wst = i
        if wst == -1:
            terminals[2] = terminals[2] + 1
            wst = bin + 1
        terminals[wst] = terminals[wst] + nw

    # With directory name, we store all our fitness cases
    # NOTE: This is specific to the problem, this should change
    # in a different problem if needed

    def initCases(self):
        # This will contain test names
        self.test_names = []
        # This will contain test size n, number of objects
        self.test_n = []
        # This will contain test val c, capacity of bins
        self.test_c = []
        # This will contain test object values for each test
        self.test_objs = []
        # Iterate over every file in our directory
        for filename in os.listdir(self.dir):
            # We just check bpp test files
            if not "bpp" in filename:
                continue
            # TODO: DELETE THIS
            # WE SKIP JUST FOR SMALL TESTING PURPOSES
            if len(self.test_names) > 1:
                continue
            # Store test name
            self.test_names.append(filename)
            # Get test contents
            file = open(self.dir + filename, 'r')
            content = file.read()
            # Parse contents and store them in list as ints
            nums = re.findall(r'\d+', content)
            nums = list(map(int, nums))
            # Store relevant information
            self.test_n.append(nums[0])
            self.test_c.append(nums[1])
            self.test_objs.append(nums[2:])
            # Make sure tests are ok, n == total objs
            assert(nums[0] == len(nums[2:]))

    # Function to evaluate the fitness of a specific population
    # - population = List with Population, each element representing a
    # chromosome generated in process
    # Return values obtained in a list
    def evaluatePopulationFitness(self, population):
        waste = []
        for ind in population:
            waste.append(self.evaluateChromosomeFitness(ind, 0))
        # Get max waste to normalize fitness
        mxwaste = max(waste)
        return list(map(lambda x: 1 - (x / mxwaste) + 0.1, waste))

    # Evaluates fitness of an individual, by evaluating each one of our
    # test cases, and getting and average of evaluations
    # - ind = Individual chromosome used to evaluate fitness
    # - f = Flag used for printing if necessary
    def evaluateChromosomeFitness(self, ind, f):
        print("Eval chromosome fitness")  # DEL
        waste = []
        # For each test, we get fitness
        for i in range(0, len(self.test_names)):
            waste.append(self.evalFitnessCase(ind, i))
        avgwaste = sum(waste) / len(waste)
        return avgwaste

    # Evaluate a chromosome in a specific test
    # - ind = Individual chromosome used to evaluate fitness
    # - idx = Index of test used
    # This function is also specific to the problem in hand
    # It needs for test cases to all have the same size
    # In this case we have 20 objects
    # If we change, it does not work
    def evalFitnessCase(self, ind, idx):
        print("Eval case fitness", idx)  # DEL
        # We setup our "environment"
        # This is the terminals that the problem will use for its expression
        # We have a list of length 24
        # First element is N
        # Second element is C
        # Third element is current # of bins used
        # Fourth element is arriving object weigth
        terminals = [self.test_n[idx], self.test_c[idx], 1, 0]
        # Next 20 elements are the N possible bins we can have at the end
        # each with its current occupancy
        terminals.extend([0] * self.test_n[idx])

        # Now we simulate each items arrival
        for item in self.test_objs[idx]:
            # Update terminals with given object
            terminals[3] = item

            # Pick heuristic with gene expression and with given terminals
            heuristic = self.chooseHeuristic(ind, terminals)

            # Check which heuristic to use and do it
            self.heuristics[heuristic](terminals)

        # After all simulation, we calculate fitness with our formula
        # We get all wasted space
        waste = 0
        bin = terminals[2] + 4
        C = terminals[1]
        for i in range(4, bin):
            waste = waste + C - terminals[i]

        return waste

    def chooseHeuristic(self, ind, terminals):
        # TODO: IMPLEMENT EXPRESSION AND CONSEQUENT CHOOSE OF HEURISTIC
        # Currently always uses next fit
        return self.gene_expressor.express(ind, terminals)
