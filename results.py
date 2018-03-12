import matplotlib.pyplot as plt
import numpy as np


def show_results(best_genotype, avg_pop_fit, best_genotype_in_pop_fit, positive, negative, scope):
    scope = scope/2 * 1.2
    plt.title(f"Best genotype -> fitness: {best_genotype[1]} ,  generation: {best_genotype[2]}")
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
    plt.plot(best_genotype_in_pop_fit, "g")
    plt.show()

    print(best_genotype)


def show_results_allcases(best_genotypes, avg_pop_fit, best_genotype_in_pop_fit, positive, negative, scope):
    scope = scope/2 * 1.2
    for best_genotype in best_genotypes:
        plt.title(f"Best genotype (S={best_genotype[3]},C={best_genotype[4]},M={best_genotype[5]}) -> fit={best_genotype[1]} , gen: {best_genotype[2]}")
        axes = plt.gca()
        axes.set_xlim([-scope, scope])
        axes.set_ylim([-scope, scope])
        plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',
                 np.arange(-scope, scope, 0.01), np.polyval(best_genotype[0], np.arange(-scope, scope, 0.01)))
        plt.show()

    plt.title("Average fitness")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")

    for avg_fit in avg_pop_fit:
        plt.plot(avg_fit)
    plt.show()

    plt.title("Max fitness")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    for bg in best_genotype_in_pop_fit:
        plt.plot(bg)
    plt.show()




