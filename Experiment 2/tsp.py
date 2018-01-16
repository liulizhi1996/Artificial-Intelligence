import random
import math
from matplotlib import pyplot as plt


def construct_distance_matrix(points):
    dist = list()
    for i, point1 in enumerate(points):
        dist.append([])
        for j, point2 in enumerate(points):
            d = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
            dist[i].append(d)

    return dist


def partially_mapped_crossover(parent1, parent2):
    """
    See http://www.dca.fee.unicamp.br/~gomide/courses/EA072/artigos/Genetic_Algorithm_TSPR_eview_Larranaga_1999.pdf
    """
    length = len(parent1)
    cutting_point = random.sample(list(range(1, length)), 2)
    cutting_point1 = cutting_point[0]
    cutting_point2 = cutting_point[1]
    if cutting_point1 > cutting_point2:
        cutting_point1, cutting_point2 = cutting_point2, cutting_point1

    offspring1 = list()
    offspring2 = list()
    portion1 = parent1[cutting_point1:cutting_point2]
    portion2 = parent2[cutting_point1:cutting_point2]

    for i in range(cutting_point1):
        replace = parent1[i]
        while replace in portion2:
            idx = portion2.index(replace)
            replace = portion1[idx]
        offspring1.append(replace)

        replace = parent2[i]
        while replace in portion1:
            idx = portion1.index(replace)
            replace = portion2[idx]
        offspring2.append(replace)

    offspring1 += portion2
    offspring2 += portion1

    for i in range(cutting_point2, length):
        replace = parent1[i]
        while replace in portion2:
            idx = portion2.index(replace)
            replace = portion1[idx]
        offspring1.append(replace)

        replace = parent2[i]
        while replace in portion1:
            idx = portion1.index(replace)
            replace = portion2[idx]
        offspring2.append(replace)

    return offspring1, offspring2


def genetic_algorithm(dist):
    vertex_num = len(dist)

    # Initialization
    population_size = 500
    population = list()
    for i in range(population_size):
        candidate = list(range(0, vertex_num))
        random.shuffle(candidate)
        population.append(candidate)

    for gen in range(2000):
        # Roulette wheel selection
        # step 1: Fitness
        fitness = list()
        alpha = 100
        for candidate in population:
            f = alpha / sum([dist[candidate[i]][candidate[(i+1) % vertex_num]] for i in range(vertex_num)])
            fitness.append(f)

        # step 2: compute probability to be selected
        fitness_sum = sum(fitness)
        probability = [f / fitness_sum for f in fitness]

        # step 3: compute cumulative probability
        cumulative_probability = list()
        for i in range(population_size):
            cum_prob = sum(probability[:(i+1)])
            cumulative_probability.append(cum_prob)

        selection = list()
        for k in range(population_size):
            # step 4: pick a random number from [0, 1]
            r = random.random()

            # step 5: choose one candidate
            choice = 0
            for i in range(1, population_size):
                if cumulative_probability[i-1] <= r <= cumulative_probability[i]:
                    choice = i
                    break
            selection.append(population[choice])

        # Crossover
        # step 1: pair two candidates, (0, 1), (2, 3), ...
        probability_crossover = 0.7
        crossover = list()
        random.shuffle(selection)
        for k in range(population_size//2):
            # step 2: partially-mapped crossover (PMX)
            r = random.random()
            if r < probability_crossover:
                new_candidate1, new_candidate2 = partially_mapped_crossover(selection[k], selection[k+1])
                crossover.append(new_candidate1)
                crossover.append(new_candidate2)
            else:
                crossover.append(selection[k])
                crossover.append(selection[k+1])

        # Mutation
        probability_mutation = 0.005
        mutation = list()
        for k, candidate in enumerate(crossover):
            r = random.random()
            if r < probability_mutation:
                # step 1: choose mutation point
                mutation_point_1 = random.randint(0, vertex_num-1)
                mutation_point_2 = random.randint(0, vertex_num-1)
                # step 2: swap two point
                new_candidate = candidate
                new_candidate[mutation_point_1], new_candidate[mutation_point_2] = \
                    new_candidate[mutation_point_2], new_candidate[mutation_point_1]
                mutation.append(new_candidate)
            else:
                mutation.append(candidate)

        population = mutation
        population_size = len(population)

    fitness = list()
    for candidate in population:
        f = sum([dist[candidate[i]][candidate[(i + 1) % vertex_num]] for i in range(vertex_num)])
        fitness.append(f)
    idx = fitness.index(min(fitness))
    return population[idx], fitness[idx]


if __name__ == "__main__":
    # data set from http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/burma14.tsp.gz
    cities = [(16.47, 96.10),
              (16.47, 94.44),
              (20.09, 92.54),
              (22.39, 93.37),
              (25.23, 97.24),
              (22.00, 96.05),
              (20.47, 97.02),
              (17.20, 96.29),
              (16.30, 97.38),
              (14.05, 98.12),
              (16.53, 97.38),
              (21.52, 95.59),
              (19.41, 97.13),
              (20.09, 94.55)]

    dist = construct_distance_matrix(cities)
    path, total = genetic_algorithm(dist)
    path_point_x = [cities[idx][0] for idx in path] + [cities[path[0]][0]]
    path_point_y = [cities[idx][1] for idx in path] + [cities[path[0]][1]]
    print(path)
    print(total)

    plt.plot(path_point_x, path_point_y, 'b')
    plt.plot(path_point_x, path_point_y, 'ro')
    plt.show()
