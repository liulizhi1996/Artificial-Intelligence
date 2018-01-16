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


def swap(path):
    permutation = list(range(len(path)))
    random.shuffle(permutation)
    path[permutation[0]], path[permutation[1]] = path[permutation[1]], path[permutation[0]]
    return path


def inverse(path):
    permutation = list(range(len(path)))
    random.shuffle(permutation)
    pos1 = permutation[0]
    pos2 = permutation[1]
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    if pos1 > 0:
        path = path[:pos1] + path[pos2:pos1-1:-1] + path[pos2+1:]
    else:
        path = path[pos2::-1] + path[pos2+1:]
    return path


def shift(path):
    permutation = list(range(len(path)))
    random.shuffle(permutation)
    pos1 = permutation[0]
    pos2 = permutation[1]
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    if pos2 < len(path)-1:
        path = path[:pos1] + [path[pos2+1]] + path[pos1:pos2+1] + path[pos2+2:]
    return path


def simulated_annealing(dist):
    temperature = 10
    min_temperature = 0.00001
    speed = 0.9999

    # initial state
    vertex_num = len(dist)
    path = list(range(vertex_num))
    random.shuffle(path)
    distance = sum([dist[path[i]][path[i+1]] for i in range(vertex_num-1)] + [dist[path[-1]][path[0]]])

    # loop
    while temperature > min_temperature:
        # pick a random neighbour
        r = random.uniform(0, 1)
        if 0 <= r < 1/3:
            new_path = swap(path)
        elif 1/3 <= r < 2/3:
            new_path = inverse(path)
        else:
            new_path = shift(path)
        new_distance = sum([dist[new_path[i]][new_path[i + 1]] for i in range(vertex_num - 1)] +
                           [dist[new_path[-1]][new_path[0]]])

        # selection
        if new_distance <= distance:
            path = new_path
            distance = new_distance
        else:
            r = random.uniform(0, 1)
            if r < math.exp(-(new_distance - distance) / temperature):
                path = new_path
                distance = new_distance

        # cool down
        temperature *= speed

    return path, distance


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
    path, total = simulated_annealing(dist)
    print(path)
    print(total)

    path_point_x = [cities[idx][0] for idx in path] + [cities[path[0]][0]]
    path_point_y = [cities[idx][1] for idx in path] + [cities[path[0]][1]]
    plt.plot(path_point_x, path_point_y, 'b')
    plt.plot(path_point_x, path_point_y, 'ro')
    plt.show()
