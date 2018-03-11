import numpy as np
import fitness as f


def gen0(amount, degree, positive, negative, coeff_range):
    """ Generates random polynomial and calculates it's fitness """
    population = []
    for i in range(amount):
        genotype = generate_genotype(coeff_range, degree)
        fitness = f.calculate_fitness(genotype, positive, negative)
        arr = [genotype, fitness]
        population.append(arr)

    return sorted(population, key=lambda x: x[1], reverse=True)


def generate_genotype(coeff_range, degree):
    return np.random.random(degree+1) * coeff_range - coeff_range/2