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


def main():
    function_set = [add, sub, mul, div]
    terminal_set_sz = 24
    generations = 100
    population_size = 30
    adf_gene_cnt = 6
    class_cnt = 4
    pop = Population(generations, population_size, adf_gene_cnt, class_cnt, 24, function_set,
                     terminal_set_sz, './../training/')

    pop.run()


main()
