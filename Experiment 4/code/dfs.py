import collections
import auxiliary


def depth_first_search(initial_state, goal_state):
    stack = collections.deque()
    closed_set = set()
    come_from = dict()

    stack.append(initial_state)
    come_from[initial_state] = None

    while len(stack) > 0:
        state = stack.pop()

        if state in closed_set:
            continue

        if state == goal_state:
            return auxiliary.construct_path(come_from, state)

        closed_set.add(state)
        for child_state in auxiliary.get_children(state):
            if child_state not in come_from.keys():
                come_from[child_state] = state
            stack.append(child_state)


def depth_first_search_recursive(initial_state, goal_state):
    def dfs(path):
        if path[-1] == goal_state:
            return path
        for child_state in auxiliary.get_children(path[-1]):
            if child_state not in path:
                new_path = dfs(path + [child_state])
                if new_path:
                    return new_path
        return None

    return dfs([initial_state])


if __name__ == "__main__":
    initial = ((2, 8, 1), (4, 6, 3), (0, 7, 5))
    goal = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
    path = depth_first_search(initial, goal)
    auxiliary.print_path(path)
    '''
    initial = ((1, 2, 3), (0, 8, 4), (7, 6, 5))
    goal = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
    path = depth_first_search_recursive(initial, goal)
    auxiliary.print_path(path)
    '''
