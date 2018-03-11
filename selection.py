import numpy as np


def selection(population, s_type):
    if s_type == 1:
        return selection_prob(population)
    if s_type == 2:
        return selection_random(population)
    if s_type == 3:
        return selection_tournament(population)


""" SELECTION BASED ON PROBABILITY """


def selection_prob(population):
    while True:
        g1 = select1_prob(population)
        g2 = select1_prob(population)
        if g1[1] != g2[1] or g1[0][0] != g2[0][0]:
            return g1, g2


def select1_prob(population):
    fit_sum = 0
    for genotype in population:
        fit_sum = fit_sum + genotype[1]
    prob = np.random.rand(1) * fit_sum
    fit_sum = 0
    for genotype in population:
        g1 = genotype
        fit_sum = fit_sum + genotype[1]
        if fit_sum >= prob:
            return g1


""" RANDOM SELECTION """


def selection_random(population):
    # TODO: Figure out why equality check does not work
    g1 = population[np.random.randint(len(population))]
    g2 = population[np.random.randint(len(population))]
    return g1, g2


""" TOURNAMENT SELECTION SELECTION """


def selection_tournament(population):
    g1 = population[np.random.randint(len(population))]
    g2 = population[np.random.randint(len(population))]
    g3 = population[np.random.randint(len(population))]
    g4 = population[np.random.randint(len(population))]
    g1_win = g1
    g2_win = g3
    if g1[1] != g2[1] or g1[0][0] != g2[0][0]:
        if g1[1] < g2[1]:
            g1_win = g2

    if g3[1] != g4[1] or g3[0][0] != g4[0][0]:
        if g3[1] < g4[1]:
            g2_win = g4

    return g1_win, g2_win
