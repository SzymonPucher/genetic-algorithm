import numpy as np
import fitness as f


def crossover(degree, g1, g2, positive, negative, c_type):
    if c_type == 1:
        return crossover_random(degree, g1, g2, positive, negative)
    if c_type == 2:
        return crossover_split(degree, g1, g2, positive, negative)


def crossover_random(degree, g1, g2, positive, negative):
    new_genotype = []
    j = 0
    cross_array = np.random.randint(2, size=degree + 1)
    for i in cross_array:
        if i:
            new_genotype.append(g1[0][j])
        else:
            new_genotype.append(g2[0][j])
        j = j + 1

    # print(g1, g2)
    ng = [np.asarray(new_genotype), f.calculate_fitness(new_genotype, positive, negative)]
    return ng


def crossover_split(degree, g1, g2, positive, negative):
    new_genotype = []
    j = 0
    rand = np.random.randint(degree)
    cross_array = np.random.randint(2, size=degree+1)
    for i in cross_array:
        if j > rand:
            new_genotype.append(g1[0][j])
        else:
            new_genotype.append(g2[0][j])
        j = j + 1

    # print(g1, g2)
    ng = [np.asarray(new_genotype), f.calculate_fitness(new_genotype, positive, negative)]
    return ng