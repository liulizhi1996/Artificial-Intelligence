import collections
import auxiliary


def breadth_first_search(initial_state, goal_state):
    open_set = collections.deque()
    closed_set = set()
    come_from = dict()

    open_set.append(initial_state)
    come_from[initial_state] = None

    while len(open_set) > 0:
        state = open_set.popleft()

        if state == goal_state:
            return auxiliary.construct_path(come_from, state)

        for child_state in auxiliary.get_children(state):
            if child_state in closed_set:
                continue
            if child_state not in open_set:
                come_from[child_state] = state
                open_set.append(child_state)

        closed_set.add(state)


if __name__ == "__main__":
    initial = ((2, 8, 1), (4, 6, 3), (0, 7, 5))
    goal = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
    # initial = ((8, 6, 7), (2, 5, 4), (3, 0, 1))
    # goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    path = breadth_first_search(initial, goal)
    auxiliary.print_path(path)
