
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
import copy

import points
import selection as s
import crossover as c
import mutation as m
import fitness as f


def gen0(amount, degree, positive, negative):
    """ Generates random polynomial and calculates it's fitness """
    population = []
    for i in range(amount):
        genotype = np.random.random(degree+1) * 4 - 2
        fitness = f.calculate_fitness(genotype, positive, negative)
        arr = [genotype, fitness]
        population.append(arr)

    return sorted(population, key=lambda x: x[1], reverse=True)


def results(best_genotype, avg_pop_fit, best_genotype_in_pop_fit):
    plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',
             np.arange(-1, 1, 0.01), np.polyval(best_genotype[0], np.arange(-1, 1, 0.01)))
    plt.show()

    plt.plot(avg_pop_fit)
    plt.show()

    plt.plot(best_genotype_in_pop_fit)
    plt.show()

    print(best_genotype)


def init(no_of_gt_in_pop, degree, positive, negative, no_of_generations):
    """ Generating population 0 """
    population = gen0(no_of_gt_in_pop, degree, positive, negative)
    """ Best genotype, average fitness of whole population and best genotype in population initialized """
    best_genotype = [population[0][0], population[0][1], 0]
    avg_pop_fit = [f.avg_pop_fitness(population, no_of_gt_in_pop)]
    best_genotype_in_pop_fit = [population[0][1]]

    """ Generations """
    for generation in range(1, no_of_generations+1):
        """ Initialize new population """
        new_population = []
        """ Creating new population """
        while len(new_population) < no_of_gt_in_pop:
            """ SELECTION """
            g1, g2 = s.selection(population)

            rand = np.random.randint(3)
            if rand == 1:
                """ CROSSOVER """
                new_population.append(c.crossover(degree, g1, g2, positive, negative))

            if rand == 2:
                """ MUTATION """
                new_population.append(m.mutation(degree, g1, positive, negative))
        """ Preparing for next generation, saving avg fitness and best genotype in generation """
        population = copy.deepcopy(new_population)
        population = sorted(population, key=lambda x: x[1], reverse=True)
        avg_pop_fit.append(f.avg_pop_fitness(population, no_of_gt_in_pop))
        best_genotype_in_pop_fit.append(population[0][1])
        """ Checking if current generation has better genotype """
        if best_genotype[1] < population[0][1]:
            best_genotype = [population[0][0], population[0][1], generation]

    """ Showing results """
    results(best_genotype, avg_pop_fit, best_genotype_in_pop_fit)



#positive, negative = points.generate_points_random(100)
positive, negative = points.generate_points_fx(10)
#positive, negative = points.generate_points_radius(100)
init(10, 5, positive, negative, 100)

#print(f.calculate_fitness_dist(gen0(3,3,positive,negative), positive, negative))
