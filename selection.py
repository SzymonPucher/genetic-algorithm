import numpy as np


def select2nd(population, prob, g1):
    c = 0
    for genotype in population:
        g2 = genotype
        c = c + genotype[1]
        if c > prob:
            if g1[1] == g2[1]:
                continue
            break

    return g2


def selection(population):
    c = 0
    for genotype in population:
        c = c + genotype[1]
    prob = np.random.rand(1) * c
    c = 0
    for genotype in population:
        g1 = genotype
        c = c + genotype[1]
        if c > prob:
            break

    prob = np.random.rand(1) * c

    g2 = select2nd(population, prob, g1)

    return g1, g2
