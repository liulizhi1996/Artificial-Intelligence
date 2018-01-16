import auxiliary


def dist_between(state1, state2):
    return auxiliary.manhattan_distance(state1, state2)


def heuristic_cost_estimate(state, goal_state):
    return auxiliary.manhattan_distance(state, goal_state)


def iterative_deepening_a_star(initial_state, goal_state):
    def search(path, g, bound):
        node = path[-1]
        f = g + heuristic_cost_estimate(node, goal_state)
        if f > bound:
            return path, f
        if node == goal_state:
            return path, True
        min_bound = float('inf')
        for child_state in auxiliary.get_children(node):
            if child_state not in path:
                path, t = search(path+[child_state], g+dist_between(node, child_state), bound)
                if t == True:
                    return path, t
                if t < min_bound:
                    min_bound = t
                path = path[:-1]
        return path, min_bound

    bound = heuristic_cost_estimate(initial_state, goal_state)

    while True:
        new_path, new_bound = search([initial_state], 0, bound)
        if new_bound == True:
            return new_path
        if new_bound == float('inf'):
            return []
        bound = new_bound


if __name__ == "__main__":
    # initial = ((2, 8, 1), (4, 6, 3), (0, 7, 5))
    # goal = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
    initial = ((8, 6, 7), (2, 5, 4), (3, 0, 1))
    goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    path = iterative_deepening_a_star(initial, goal)
    auxiliary.print_path(path)
