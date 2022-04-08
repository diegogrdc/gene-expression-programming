from Chromosome import Chromosome


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def main():
    print("Multi Cellular System - Multiple Outputs")
    x = Chromosome(2, [add, sub], [])


main()
