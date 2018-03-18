
def get_config():
    """
    p_type:
        1 = random
        2 = based of f(x) = x, if above then + else -
        3 = within some radius around initial points, seperate for +/-
    f_type:
        1 = binary
    s_type:
        1 = probability based on fitness
        2 = random
        3 = torunament
    c_type:
        1 = random coefficients
        2 = split
    m_type:
        1 = random coefficient replaced by random number
        2 = binary mutation
    :return: run configuration`
    """
    p_type, f_type, s_type, c_type, m_type = 3, 1, 3, 1, 2
    no_of_points = 100
    scope = 2
    no_of_genotypes_in_population = 20
    degree_of_genotype = 5
    coeff_range_of_genotype = 4
    no_of_generations = 100
    return p_type, f_type, s_type, c_type, m_type,\
           no_of_points, scope, no_of_genotypes_in_population, degree_of_genotype, coeff_range_of_genotype, no_of_generations


def get_config_all_cases():
    show_only_best_genotype_for_given_p_type = False
    p_type, f_type, s_type, c_type, m_type = 1, 1, 1, 1, 1
    no_of_points = 100
    scope = 2
    no_of_genotypes_in_population = 50
    degree_of_genotype = 5
    coeff_range_of_genotype = 10
    no_of_generations = 100

    return p_type, f_type, s_type, c_type, m_type, show_only_best_genotype_for_given_p_type,\
           no_of_points, scope, no_of_genotypes_in_population, degree_of_genotype, coeff_range_of_genotype, no_of_generations
