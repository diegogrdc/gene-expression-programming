# Class created to express genes
# This involves simulating the gene expression with a
# specific set of terminals, and return the values of each
# one of the classes evaluated on the gene
class GeneExpressor:

    # Init gene expresson
    # - function_set = Functions used in gene expression
    def __init__(self, function_set):
        self.function_set = function_set

    # Express a gene with given terminals
    # - gene = Gene to express (list)
    # - terminals = Terminal values used on this expression
    def express(self, gene, terminals):
        print("Expressing Gene", gene)  # DEL
        # We first need to express all ADFS and get
        # their vals in case we need them on the home-
        # otic evaluation
        adfs = []
        for adf in gene.adfs:
            adfs.append(self.expressADF(adf, terminals))
        # Each val represents a class
        vals = []
        # We will express each "homeotic gene"
        for hom in gene.genes:
            vals.append(self.expressHomeotic(hom, terminals, adfs))
        # We return value for all classes
        return vals

    # Express a specific homeotic gene with given terminals
    # - hom = Homeotic Gene to express
    # - terminals = Terminal values used on this expression
    # - adfs = ADFS vals already evaluated to use as constants
    def expressHomeotic(self, hom, terminals, adfs):
        # Special case where first position is a terminal
        if hom[0][0] == 'a':
            return adfs[hom[0][1]]
        # If not, we need to create tree
        # and generate references to values used as params
        queue = []
        params = []
        for i in range(0, len(hom)):
            # For each position, we first assign
            # an empty list of params
            params.append([])
            # Check if we can skip
            if len(queue) == 0 and i > 0:
                continue
            # If we have a function we get param size
            # and lazily assign references as we advance
            if hom[i][0] == 'f':
                param_sz = self.fn_param_sz(self.function_set[hom[i][1]])
                # We need param_sz params, so we will need this
                # index param_sz times on the queue
                queue.extend([i] * param_sz)
            # Any position apart from first one should be
            # evaluated by upper nodes
            if i > 0:
                to = queue.pop(0)
                params[to].append(i)
        # Having calculated params, we use this to recursively calculate the value
        return self.getExpressionVal(hom, 0, terminals, adfs, params)

    # Express a specific adf gene with given terminals
    # - hom = Homeotic Gene to express
    # - terminals = Terminal values used on this expression
    def expressADF(self, adf, terminals):
        # Special case where first position is a terminal
        if adf[0][0] == 't':
            return terminals[adf[0][1]]
        # If not, we need to create tree
        # and generate references to values used as params
        queue = []
        params = []
        for i in range(0, len(adf)):
            # For each position, we first assign
            # an empty list of params
            params.append([])
            # Check if we can skip
            if len(queue) == 0 and i > 0:
                continue
            # If we have a function we get param size
            # and lazily assign references as we advance
            if adf[i][0] == 'f':
                param_sz = self.fn_param_sz(self.function_set[adf[i][1]])
                # We need param_sz params, so we will need this
                # index param_sz times on the queue
                queue.extend([i] * param_sz)
            # Any position apart from first one should be
            # evaluated by upper nodes
            if i > 0:
                to = queue.pop(0)
                params[to].append(i)
        # Having calculated params, we use this to recursively calculate the value
        return self.getExpressionVal(adf, 0, terminals, [], params)

    # With tree generated, we evaluate recursively
    # to get value of our gene
    # - hom = Homeotic gene being evaluated
    # - idx = Position currently evaluated
    # - terminals = terminal values
    # - adfs = adf values
    # - params = list with position to the values used in expressin
    # a specific function
    def getExpressionVal(self, hom, idx, terminals, adfs, params):
        # If not function, just return val depending
        # on if it is terminal or adf
        if hom[idx][0] != 'f':
            # Terminal
            if hom[idx][0] == 't':
                return terminals[hom[idx][1]]
            # ADF
            else:
                return adfs[hom[idx][1]]
        # Else, get all params and evaluate function
        param = params[idx]
        # For each param, we convert it into a value
        vals = []
        for p in param:
            # Eval position recursively
            vals.append(self.getExpressionVal(hom, p, terminals, adfs, params))
        # Eval functions with all its params evaluated now
        val = self.function_set[hom[idx][1]](*vals)
        return val

    # Return # of params a function needs
    # fn - Function we will eval
    def fn_param_sz(self, fn):
        return fn.__code__.co_argcount
