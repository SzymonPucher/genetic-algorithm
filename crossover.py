import numpy as np
import fitness as f


def crossover(degree, g1, g2, positive, negative):
    new_genotype = []
    j = 0
    for i in np.random.randint(2, size=degree+1):
        if i:
            new_genotype.append(g1[0][j])
        else:
            new_genotype.append(g2[0][j])
        j = j + 1

    # print(g1, g2)
    ng = [np.asarray(new_genotype), f.calculate_fitness(new_genotype, positive, negative)]
    return ng
