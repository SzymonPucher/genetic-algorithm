import matplotlib.pyplot as plt
import numpy as np


def show_results(best_genotype, avg_pop_fit, best_genotype_in_pop_fit, positive, negative, scope, p_type):
    if p_type != 3:
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


def show_results_allcases(best_genotypes, avg_pop_fit, best_genotype_in_pop_fit, positive, negative, scope, p_type, types, show_type):
    if p_type != 3:
        scope = scope/2 * 1.2
    if show_type:
        best_genotypes = sorted(best_genotypes, key=lambda x: x[1], reverse=True)
        plt.title(
            f"Best genotype (S={best_genotypes[0][3]},C={best_genotypes[0][4]},M={best_genotypes[0][5]}) -> fit={best_genotypes[0][1]} , gen: {best_genotypes[0][2]}")
        axes = plt.gca()
        axes.set_xlim([-scope, scope])
        axes.set_ylim([-scope, scope])
        plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',
                 np.arange(-scope, scope, 0.01), np.polyval(best_genotypes[0][0], np.arange(-scope, scope, 0.01)))
        plt.show()
    else:
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
    colors = ['#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#d2f53c', '#800000', '#000080', '#000000']
    i = 0
    for avg_fit in avg_pop_fit:
        plt.plot(avg_fit, colors[i], label=f"{types[i][0]},{types[i][1]},{types[i][2]}")
        i = i + 1

    plt.legend(loc='best', fancybox=True, framealpha=0.5)
    plt.show()

    plt.title("Max fitness")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    i = 0
    for bg in best_genotype_in_pop_fit:
        plt.plot(bg, colors[i], label=f"{types[i][0]},{types[i][1]},{types[i][2]}")
        i = i + 1
    plt.legend(loc='best', fancybox=True, framealpha=0.5)
    plt.show()


def plot_points(positive, negative):
    plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',)
    plt.show()


