from collections import deque


def is_valid(state):
    """
    Check if the state is valid
    :param state: three-tuple (M, C, B), which represents current state of left bank
    :return: True or False
    """
    missionaries = state[0]
    cannibals = state[1]
    if missionaries == 0:
        return True
    elif missionaries >= cannibals:
        return True
    else:
        return False


def generate_successor(state, total_missionaries, total_cannibals, boat_capacity):
    """
    Generate valid successors of state
    :param state: three-tuple (M, C, B), which represents current state of left bank
    :param total_missionaries: the total of missionaries
    :param total_cannibals: the total of cannibals
    :param boat_capacity: capacity of the boat
    :return: various of successor state
    """
    left_bank = state
    right_bank = (total_missionaries - state[0], total_cannibals - state[1], 1 - state[2])

    if left_bank[2] == 1:   # boat on the left bank
        for missionary_passengers in range(0, min([left_bank[0], boat_capacity])+1):
            for cannibal_passengers in range(0, min([left_bank[1], boat_capacity-missionary_passengers])+1):
                if missionary_passengers == 0 and cannibal_passengers == 0:
                    continue
                new_state = (left_bank[0]-missionary_passengers, left_bank[1]-cannibal_passengers, 0)
                if not is_valid(new_state):
                    continue
                boat = (missionary_passengers, cannibal_passengers, None)
                if not is_valid(boat):
                    continue
                new_right_bank = (right_bank[0]+missionary_passengers, right_bank[1]+cannibal_passengers, 1)
                if not is_valid(new_right_bank):
                    continue
                yield new_state
    else:                   # boat on the right bank
        for missionary_passengers in range(0, min([right_bank[0], boat_capacity])+1):
            for cannibal_passengers in range(0, min([right_bank[1], boat_capacity-missionary_passengers])+1):
                if missionary_passengers == 0 and cannibal_passengers == 0:
                    continue
                new_state = (left_bank[0]+missionary_passengers, left_bank[1]+cannibal_passengers, 1)
                if not is_valid(new_state):
                    continue
                boat = (missionary_passengers, cannibal_passengers, None)
                if not is_valid(boat):
                    continue
                new_right_bank = (right_bank[0]-missionary_passengers, right_bank[1]-cannibal_passengers, 0)
                if not is_valid(new_right_bank):
                    continue
                yield new_state


def construct_path(state, come_from):
    """
    Construct path end with state
    :param state: end of path
    :param come_from: a dict, key (child state) -> parent state
    :return: a solution path from initial state to goal
    """
    path = list()

    while state is not None:
        path.append(state)
        state = come_from[state]

    path.reverse()
    return path


def print_path(path, total_missionaries, total_cannibals):
    """
    Print solution intuitively
    :param path: solution path from initial state to goal
    :param total_missionaries: the total of missionaries
    :param total_cannibals: the total of cannibals
    :return: no return value
    """
    for idx, state in enumerate(path):
        left_bank = state
        right_bank = (total_missionaries - state[0], total_cannibals - state[1], 1 - state[2])
        print("Trip %d:" % idx)
        print("+  Left Bank  +  River  +  Right Bank  +")
        if left_bank[2] == 1:
            print("|    M:%2d     | ◆       |     M:%2d     |" % (left_bank[0], right_bank[0]))
            print("|    C:%2d     |         |     C:%2d     |" % (left_bank[1], right_bank[1]))
        else:
            print("|    M:%2d     |       ◆ |     M:%2d     |" % (left_bank[0], right_bank[0]))
            print("|    C:%2d     |         |     C:%2d     |" % (left_bank[1], right_bank[1]))
        print()


def cross_river(total_missionaries, total_cannibals, boat_capacity):
    """
    Solve missionaries and cannibals problem, when there are total_missionaries missionaries,
    total_cannibals cannibals and the boat's capacity is boat_capacity
    :param total_missionaries: the total of missionaries
    :param total_cannibals: the total of cannibals
    :param boat_capacity: capacity of the boat
    :return: solution of the specific problem
    """
    open_set = deque()
    closed_set = set()
    come_from = dict()

    state = (total_missionaries, total_cannibals, 1)
    goal = (0, 0, 0)
    come_from[state] = None
    open_set.append(state)

    while len(open_set) > 0:
        state = open_set.popleft()

        if state == goal:
            return construct_path(goal, come_from)

        for child_state in generate_successor(state, total_missionaries, total_cannibals, boat_capacity):
            if child_state in closed_set:
                continue

            if child_state not in open_set:
                come_from[child_state] = state
                open_set.append(child_state)

        closed_set.add(state)

    return []


if __name__ == "__main__":
    m = 3
    n = 2
    solution = cross_river(m, m, n)
    print_path(solution, m, m)
