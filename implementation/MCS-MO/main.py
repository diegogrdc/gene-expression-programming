from pickle import FALSE
from Population import Population


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return 0
    return x / y


def ifelse(x, y, z):
    if x:
        return y
    else:
        return z


def gte(x, y):
    return x > y


def smt(x, y):
    return x < y


def ne(x, y):
    return x != y


def eq(x, y):
    return x != y


def main():
    function_set = [add, sub, mul, ifelse, gte, smt, eq, ne, div]
    terminal_set_sz = 54
    head_sz = 25
    generations = 100
    population_size = 50
    adf_gene_cnt = 25
    class_cnt = 4
    pop = Population(generations, population_size, adf_gene_cnt, class_cnt, head_sz, function_set,
                     terminal_set_sz, './prelim/HWFTRAIN/', './prelim/HWFTEST/', True)
    # pop = Population(generations, population_size, adf_gene_cnt, class_cnt, head_sz, function_set,
    #                 terminal_set_sz, './training/', './testing/', False)

    pop.run()


main()
