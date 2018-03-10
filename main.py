
"""
[Start] Generate random population of n chromosomes (suitable solutions for the problem)
[Fitness] Evaluate the fitness f(x) of each chromosome x in the population
[New population] Create a new population by repeating following steps until the new population is complete
    [Selection] Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)
    [Crossover] With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.
    [Mutation] With a mutation probability mutate new offspring at each locus (position in chromosome).
    [Accepting] Place new offspring in a new population
[Replace] Use new generated population for a further run of algorithm
[Test] If the end condition is satisfied, stop, and return the best solution in current population
[Loop] Go to step 2

---

gen = 0
initialise population 0
evaluate population 0
while gen <= genmax
    population gen+1 = selection( population gen )
    population gen+1 = crossover( population gen )
    population gen+1 = mutation( population gen )
    evaluate( population gen )
    gen++
end
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import copy


def generate_points_random(amount):
    amount = math.floor(amount / 2)
    positive = np.random.random((2, amount)) * 2 - 1
    negative = np.random.random((2, amount)) * 2 - 1
    return positive, negative


def generate_points_fx(amount):
    arr = np.random.random((amount, 2)) * 2 - 1
    xp, yp, xn, yn = [], [], [], []
    for i in range(amount):
        if arr[i][0] - arr[i][1] < 0:
            xp.append(arr[i][0])
            yp.append(arr[i][1])
        else:
            xn.append(arr[i][0])
            yn.append(arr[i][1])
    positive = [xp, yp]
    negative = [xn, yn]

    return np.asarray(positive), np.asarray(negative)


def generate_points_radius(amount):
    amount = math.floor(amount / 2)
    p1, n1 = np.random.rand(2), np.random.rand(2) * 2 - 1
    xp, yp, xn, yn = [], [], [], []


    while amount > 0:
        alpha = 2 * math.pi * np.random.rand(1)
        r = np.random.rand(1)
        x = r * math.cos(alpha) + p1[0]
        y = r * math.sin(alpha) + p1[1]
        xp.append(x)
        yp.append(y)

        alpha = 2 * math.pi * np.random.rand(1)
        r = np.random.rand(1)
        x = r * math.cos(alpha) + n1[0]
        y = r * math.sin(alpha) + n1[1]
        xn.append(x)
        yn.append(y)

        amount = amount - 1

    positive = [xp, yp]
    negative = [xn, yn]

    return np.asarray(positive), np.asarray(negative)


def generate_genotype(degree):
    genotype = np.random.random(degree+1) * 4 - 2
    return genotype


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


def crossover(degree, g1, g2):
    new_genotype = []
    j = 0
    for i in np.random.randint(2, size=degree+1):
        if i:
            new_genotype.append(g1[0][j])
        else:
            new_genotype.append(g2[0][j])
        j = j + 1

    # print(g1, g2)
    ng = [np.asarray(new_genotype), calculate_fitness(new_genotype, positive, negative)]
    return ng


def mutation(degree, genotype):
    rand = np.random.randint(degree+1)
    coefficient = np.random.rand(1) * 4 - 2
    # print(coefficient)
    g1 = copy.deepcopy(genotype)
    g1[0][rand] = coefficient
    g1[1] = calculate_fitness(g1[0], positive, negative)
    return g1


def avg_pop_fitness(population, amount):
    c = 0
    for genotype in population:
        c = c + genotype[1]
    return c/amount


def init(amount, degree, positive, negative):
    population = []

    for i in range(amount):
        genotype = generate_genotype(degree)
        fitness = calculate_fitness(genotype, positive, negative)
        arr = [genotype, fitness]
        population.append(arr)

    population = sorted(population, key=lambda x: x[1], reverse=True)
    new_population = []

    if 0:
        plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',
                 np.arange(-1, 1, 0.01), np.polyval(population[0][0], np.arange(-1, 1, 0.01)))
        plt.show()
    best_genotype = [population[0][0], population[0][1], 0]
    pop_fit = []
    for generation in range(1, 50):
        print(generation)
        count = amount
        new_population = []
        pop_fit.append(avg_pop_fitness(population, amount))
        #print(population)
        while count > 0:
            g1, g2 = selection(population)

            rand = np.random.randint(3)
            #print(rand)
            if rand == 1:
                new_genotype = crossover(degree, g1, g2)
                new_population.append(new_genotype)
                count = count - 1

            if rand == 2:
                new_genotype = mutation(degree, g1)
                new_population.append(new_genotype)
                count = count - 1

        if 0:
            plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',
                     np.arange(-1, 1, 0.01), np.polyval(population[0][0], np.arange(-1, 1, 0.01)))
            plt.show()

        #print(population)
        #print(new_population)
        pop_fit.append(avg_pop_fitness(new_population, amount))
        population = copy.deepcopy(new_population)
        population = sorted(population, key=lambda x: x[1], reverse=True)

        #print(new_population)
        if best_genotype[1] < population[0][1]:
            best_genotype = [population[0][0], population[0][1], generation]
    if 1:
        plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',
                 np.arange(-1, 1, 0.01), np.polyval(best_genotype[0], np.arange(-1, 1, 0.01)))
        plt.show()

    print(best_genotype)






#positive, negative = generate_points_random(100)
#positive, negative = generate_points_fx(100)
positive, negative = generate_points_radius(100)


init(3, 3, positive, negative)
