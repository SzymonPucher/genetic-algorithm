import numpy as np

import fitness as f
import genotype as g
import copy


def mutation(coeff_range, degree, genotype, positive, negative, m_type):
    if m_type == 1:
        return mutation_rand_coeff(degree, genotype, positive, negative, coeff_range)
    if m_type == 2:
        return mutation_bit_flip(degree, genotype, positive, negative)


""" RANDOM COEFFICIENT REPLACED BY RANDOM NUMBER"""


def mutation_rand_coeff(degree, genotype, positive, negative, coeff_range):
    g1 = copy.deepcopy(genotype)

    rand = np.random.randint(degree+1)

    g1[0][rand] = np.random.rand(1) * coeff_range - coeff_range/2
    g1[1] = f.calculate_fitness(g1[0], positive, negative)
    return g1


""" FLIPPING ONE BIT OF RANDOM COEFFICIENT"""


def mutation_bit_flip(degree, genotype, positive, negative):
    g1 = copy.deepcopy(genotype)

    rand = np.random.randint(degree + 1)

    g1[0][rand] = bit_flip(g1[0][rand])
    g1[1] = f.calculate_fitness(g1[0], positive, negative)

    return g1


def bit_flip(old_num):
    old_num = int(old_num * 10 ** 6)
    b_coeff = bin(int(old_num))
    num = np.random.randint(2, len(b_coeff))
    new_coeff = ""
    for bit in b_coeff:
        if num == 0:
            if bit == "1":
                new_coeff += "0"
            else:
                new_coeff += "1"
        else:
            new_coeff += bit
        num = num - 1

    res_coeff = int(new_coeff, 2)
    res_coeff = res_coeff / 10 ** 6
    return res_coeff