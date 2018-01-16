from collections import deque
import auxiliary


def bidirectional_search(initial_state, goal_state):
    queue_from_initial = deque()
    queue_from_goal = deque()
    come_from_initial = dict()
    come_from_goal = dict()

    queue_from_initial.append(initial_state)
    come_from_initial[initial_state] = None
    queue_from_goal.append(goal_state)
    come_from_goal[goal_state] = None

    while len(queue_from_initial) > 0 and len(queue_from_goal) > 0:
        if len(queue_from_initial) > 0:
            current_state = queue_from_initial.popleft()
            if current_state in come_from_goal:
                path_from_initial = auxiliary.construct_path(come_from_initial, current_state)
                path_from_goal = auxiliary.construct_path(come_from_goal, current_state)
                path_from_goal.reverse()
                path = path_from_initial[:-1] + path_from_goal
                return path
            for child_state in auxiliary.get_children(current_state):
                if child_state not in come_from_initial:
                    queue_from_initial.append(child_state)
                    come_from_initial[child_state] = current_state
        if len(queue_from_goal) > 0:
            current_state = queue_from_goal.popleft()
            if current_state in come_from_initial:
                path_from_initial = auxiliary.construct_path(come_from_initial, current_state)
                path_from_goal = auxiliary.construct_path(come_from_goal, current_state)
                path_from_goal.reverse()
                path = path_from_initial[:-1] + path_from_goal
                return path
            for child_state in auxiliary.get_children(current_state):
                if child_state not in come_from_goal:
                    queue_from_goal.append(child_state)
                    come_from_goal[child_state] = current_state

    return []


if __name__ == "__main__":
    # initial = ((2, 8, 1), (4, 6, 3), (0, 7, 5))
    # goal = ((1, 2, 3), (8, 0, 4), (7, 6, 5))
    initial = ((8, 6, 7), (2, 5, 4), (3, 0, 1))
    goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    path = bidirectional_search(initial, goal)
    auxiliary.print_path(path)

# http://www.geeksforgeeks.org/bidirectional-search/
