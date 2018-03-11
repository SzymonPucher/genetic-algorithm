
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

import config
import points
import selection as s
import crossover as c
import mutation as m
import fitness as f
import genotype as g


def results(best_genotype, avg_pop_fit, best_genotype_in_pop_fit, positive, negative, scope):
    scope = scope/2 * 1.2
    plt.title(f"Best genotype -> fitness = {best_genotype[1]}")
    axes = plt.gca()
    axes.set_xlim([-scope, scope])
    axes.set_ylim([-scope, scope])
    plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',
             np.arange(-scope, scope, 0.01), np.polyval(best_genotype[0], np.arange(-scope, scope, 0.01)))
    plt.show()

    plt.title("Average fitness by generation")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.plot(avg_pop_fit)
    plt.show()

    plt.title("Max fitness by generation")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.plot(best_genotype_in_pop_fit)
    plt.show()

    print(best_genotype)


def start():
    """ Configuration """
    p_type, f_type, s_type, c_type, m_type, \
    no_of_points, scope, no_of_gt_in_pop, degree, coeff_range, no_of_generations = config.get_config()
    """ Generate dataset"""
    positive, negative = points.generate_points(no_of_points, scope, p_type)
    """ Generating population 0 """
    population = g.gen0(no_of_gt_in_pop, degree, positive, negative, coeff_range)
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
            g1, g2 = s.selection(population, s_type)
            """ Randomly done crossover and mutation """
            rand = np.random.randint(3)
            if rand == 1:
                """ CROSSOVER """
                new_population.append(c.crossover(degree, g1, g2, positive, negative, c_type))
            if rand == 2:
                """ MUTATION """
                new_population.append(m.mutation(coeff_range, degree, g1, positive, negative, m_type))
        """ Preparing for next generation, saving avg fitness and best genotype in generation """
        population = copy.deepcopy(new_population)
        population = sorted(population, key=lambda x: x[1], reverse=True)
        avg_pop_fit.append(f.avg_pop_fitness(population, no_of_gt_in_pop))
        best_genotype_in_pop_fit.append(population[0][1])
        """ Checking if current generation has better genotype """
        if best_genotype[1] < population[0][1]:
            best_genotype = [population[0][0], population[0][1], generation]

    """ Showing results """
    results(best_genotype, avg_pop_fit, best_genotype_in_pop_fit, positive, negative, scope)


start()


