
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
import copy

import config
import points as p
import selection as s
import crossover as c
import mutation as m
import fitness as f
import genotype as g
import results as r


def test_standard():
    """ Configuration """
    p_type, f_type, s_type, c_type, m_type, \
    no_of_points, scope, no_of_gt_in_pop, degree, coeff_range, no_of_generations = config.get_config()
    """ Generate dataset"""
    positive, negative = p.generate_points(no_of_points, scope, p_type)
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
    r.show_results(best_genotype, avg_pop_fit, best_genotype_in_pop_fit, positive, negative, scope, p_type)


def test_all_cases():
    """ Configuration """
    p_type, f_type, s_type, c_type, m_type, show_type, \
    no_of_points, scope, no_of_gt_in_pop, degree, coeff_range, no_of_generations = config.get_config_all_cases()
    for p_type in range(1,4):
        best_genotypes = []
        avg_fit_test = []
        best_fit_test = []
        current_type = []
        while True:
            """ Generate dataset"""
            positive, negative = p.generate_points(no_of_points, scope, p_type)
            """ Generating population 0 """
            pop0 = g.gen0(no_of_gt_in_pop, degree, positive, negative, coeff_range)
            r.plot_points(positive, negative)
            inp = input("Yo, wanna this? (y/n): ")
            if inp == "y":
                break

        for s_type in range(1,4):
            for c_type in range(1, 3):
                for m_type in range(1, 3):
                    population = copy.deepcopy(pop0)
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
                    best_genotype.append(s_type)
                    best_genotype.append(c_type)
                    best_genotype.append(m_type)
                    current_type.append([s_type, c_type, m_type])
                    best_genotypes.append(best_genotype)
                    avg_fit_test.append(avg_pop_fit)
                    best_fit_test.append(best_genotype_in_pop_fit)

        """ Showing results """
        r.show_results_allcases(best_genotypes, avg_fit_test, best_fit_test, positive, negative, scope, p_type, current_type, show_type)

#test_standard()
test_all_cases()


