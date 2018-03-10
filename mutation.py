import numpy as np

import fitness as f
import copy


def mutation(degree, genotype, positive, negative):
    rand = np.random.randint(degree+1)
    coefficient = np.random.rand(1) * 4 - 2
    # print(coefficient)
    g1 = copy.deepcopy(genotype)
    g1[0][rand] = coefficient
    g1[1] = f.calculate_fitness(g1[0], positive, negative)
    return g1