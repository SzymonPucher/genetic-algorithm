import numpy as np


def calculate_fitness(genotype, positive, negative):
    total = positive.shape[1] + negative.shape[1]
    fitness = 0
    for i in range(positive.shape[1]):
        if positive[1][i] > np.polyval(genotype, positive[0][i]):
            fitness = fitness + 1

    for i in range(negative.shape[1]):
        if negative[1][i] < np.polyval(genotype, negative[0][i]):
            fitness = fitness + 1

    return fitness/total


def calculate_fitness_dist(genotype, positive, negative):
    # TODO: Fix this (still does not work properly)
    total = positive.shape[1] + negative.shape[1]
    fitness = 0
    f_arr = []
    for i in range(positive.shape[1]):
        diff = positive[1][i] - np.polyval(genotype, positive[0][i])
        f_arr.append(diff)

    for i in range(negative.shape[1]):
        diff = np.polyval(genotype, negative[0][i]) - negative[1][i]
        f_arr.append(diff)

    for fit in f_arr:
        fitness = fitness + fit[1]

    return fitness/total


def avg_pop_fitness(population, amount):
    c = 0
    for genotype in population:
        c = c + genotype[1]
    return c/amount