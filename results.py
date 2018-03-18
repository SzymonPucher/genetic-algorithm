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



    i = 0
    for g in best_genotypes:
        g.append(avg_pop_fit[i])
        g.append(best_genotype_in_pop_fit[i])
        i = i + 1

    for t in best_genotypes:
        if t[3] == 1: t[3] = "roulette"
        if t[3] == 2: t[3] = "rand"
        if t[3] == 3: t[3] = "tournament"
        if t[4] == 1: t[4] = "rand"
        if t[4] == 2: t[4] = "split"
        if t[5] == 1: t[5] = "replace"
        if t[5] == 2: t[5] = "binary"

    best_genotypes = sorted(best_genotypes, key=lambda x: x[1], reverse=True)


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

    plt.title(f"Average fitness, pgm = {p_type}")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    colors = ['#e6194b', '#3cb44b', '#ffe119', '#0082c8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#d2f53c', '#800000', '#000080', '#000000']
    i = 0
    for best_genotype in best_genotypes:
        if i == 4:
            break
        plt.plot(best_genotype[6], colors[i], label=f"{best_genotype[3]},{best_genotype[4]},{best_genotype[5]}")
        i = i + 1

    plt.legend(loc='best', fancybox=True, framealpha=0.5)
    plt.show()

    plt.title(f"Max fitness, pgm = {p_type}")
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    i = 0
    for best_genotype in best_genotypes:
        if i == 4:
            break
        plt.plot(best_genotype[7], colors[i], label=f"{best_genotype[3]},{best_genotype[4]},{best_genotype[5]}")
        i = i + 1
    plt.legend(loc='best', fancybox=True, framealpha=0.5)
    plt.show()


def plot_points(positive, negative):
    plt.plot(positive[0], positive[1], 'g+', negative[0], negative[1], 'r_',)
    plt.show()


