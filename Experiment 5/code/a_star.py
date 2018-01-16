import auxiliary


def dist_between(state1, state2):
    return auxiliary.manhattan_distance(state1, state2)


def heuristic_cost_estimate(state, goal_state):
    return auxiliary.manhattan_distance(state, goal_state)


def a_star_search(initial_state, goal_state):
    closed_set = set()
    open_set = {initial_state}
    come_from = dict()
    g_score = dict()
    f_score = dict()

    come_from[initial_state] = None
    g_score[initial_state] = 0
    f_score[initial_state] = heuristic_cost_estimate(initial_state, goal_state)

    while len(open_set) > 0:
        current_state = min([(v, k) for k, v in f_score.items() if k in open_set])[1]

        if current_state == goal_state:
            return auxiliary.construct_path(come_from, current_state)

        open_set.remove(current_state)
        closed_set.add(current_state)

        for child_state in auxiliary.get_children(current_state):
            if child_state in closed_set:
                continue

            if child_state not in open_set:
                open_set.add(child_state)

            tentative_g_score = g_score[current_state] + dist_between(current_state, child_state)
            if child_state in g_score:
                if tentative_g_score >= g_score[child_state]:
                    continue

            come_from[child_state] = current_state
            g_score[child_state] = tentative_g_score
            f_score[child_state] = g_score[child_state] + heuristic_cost_estimate(child_state, goal_state)

    return []


if __name__ == "__main__":
    # initial = ((2, 8, 1), (4, 6, 3), (0, 7, 5))
    # goal = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
    initial = ((8, 6, 7), (2, 5, 4), (3, 0, 1))
    goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    path = a_star_search(initial, goal)
    auxiliary.print_path(path)
