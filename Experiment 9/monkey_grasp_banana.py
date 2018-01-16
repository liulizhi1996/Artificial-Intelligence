from queue import deque
import copy


class State:
    def __init__(self, is_monkey_on_box, box_location, monkey_location, has_grasped):
        self.is_monkey_on_box = is_monkey_on_box
        self.box_location = box_location
        self.monkey_location = monkey_location
        self.has_grasped = has_grasped

    def go_to(self, new_location):
        if self.is_monkey_on_box is False and self.monkey_location is not None:
            self.monkey_location = new_location

    def push_box(self, new_location):
        if self.is_monkey_on_box is False and self.monkey_location == self.box_location:
            self.monkey_location = new_location
            self.box_location = new_location

    def climb_box(self):
        if self.is_monkey_on_box is False and self.monkey_location == self.box_location:
            self.is_monkey_on_box = True

    def grasp(self):
        if self.is_monkey_on_box is True and self.box_location == 'b':
            self.has_grasped = True

    def __str__(self):
        if self.is_monkey_on_box is True:
            print("Monkey is on the box.")
        else:
            print("Monkey is not on the box.")
        print("Box is at {}.".format(self.box_location))
        print("Monkey is at {}.".format(self.monkey_location))
        if self.has_grasped is True:
            print("Monkey has grasped the banana.")
        else:
            print("Monkey hasn't grasped the banana.")

    def __hash__(self):
        return hash((self.is_monkey_on_box, self.box_location, self.monkey_location, self.has_grasped))


def is_goal(state):
    if state.has_grasped:
        return True
    else:
        return False


def construct_path(state, come_from):
    action_list = list()

    while True:
        row = come_from[state]
        if row is not None:
            state = row[0]
            action = row[1]
            action_list.append(action)
        else:
            break

    action_list.reverse()

    return action_list


def get_successors(state):
    child_state = copy.deepcopy(state)
    child_state.go_to('a')
    action = "Monkey goes to a."
    if child_state != state:
        yield child_state, action

    child_state = copy.deepcopy(state)
    child_state.go_to('b')
    action = "Monkey goes to b."
    if child_state != state:
        yield child_state, action

    child_state = copy.deepcopy(state)
    child_state.go_to('c')
    action = "Monkey goes to c."
    if child_state != state:
        yield child_state, action

    child_state = copy.deepcopy(state)
    child_state.push_box('a')
    action = "Monkey pushes the box to a."
    if child_state != state:
        yield child_state, action

    child_state = copy.deepcopy(state)
    child_state.push_box('b')
    action = "Monkey pushes the box to b."
    if child_state != state:
        yield child_state, action

    child_state = copy.deepcopy(state)
    child_state.push_box('c')
    action = "Monkey pushes the box to c."
    if child_state != state:
        yield child_state, action

    child_state = copy.deepcopy(state)
    child_state.climb_box()
    action = "Monkey climbs on the box."
    if child_state != state:
        yield child_state, action

    child_state = copy.deepcopy(state)
    child_state.grasp()
    action = "Monkey grasps the banana."
    if child_state != state:
        yield child_state, action


def bfs(init_state):
    open_set = deque()
    closed_set = set()
    come_from = dict()      # key -> (parent state, action to reach child)

    come_from[init_state] = None
    open_set.append(init_state)

    while open_set:
        parent_state = open_set.popleft()

        if is_goal(parent_state):
            return construct_path(parent_state, come_from)

        for (child_state, action) in get_successors(parent_state):
            if child_state in closed_set:
                continue

            if child_state not in open_set:
                come_from[child_state] = (parent_state, action)
                open_set.append(child_state)

        closed_set.add(parent_state)

    return []


def print_path(path):
    if len(path) > 0:
        print("Solution to this problem: ")
        for idx, action in enumerate(path):
            print("{}. {}".format(idx + 1, action))
    else:
        print("No solution.")


if __name__ == "__main__":
    start = State(False, 'c', 'a', False)
    solution = bfs(start)
    print_path(solution)
