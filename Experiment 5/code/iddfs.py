import itertools
import auxiliary


def iterative_deepening_dfs(initial_state, goal_state):
    def dfs(path, depth):
        if depth == 0:
            return
        if path[-1] == goal_state:
            return path
        for state in auxiliary.get_children(path[-1]):
            if state not in path:
                new_path = dfs(path+[state], depth-1)
                if new_path:
                    return new_path

    for depth in itertools.count():
        path = dfs([initial_state], depth)
        if path:
            return path


if __name__ == "__main__":
    initial = ((2, 8, 1), (4, 6, 3), (0, 7, 5))
    goal = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
    # initial = ((8, 6, 7), (2, 5, 4), (3, 0, 1))
    # goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    path = iterative_deepening_dfs(initial, goal)
    auxiliary.print_path(path)
