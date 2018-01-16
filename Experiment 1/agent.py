from graphics import *
import random


# width of each grid
GRID_WIDTH = 25
# color list, provided for agent
COLOR = ["blue", "red", "green", "orange"]


class Agent:
    """
    An agent locates at position (agent_x, agent_y), drawn on the map using a colored circle.
    """
    def __init__(self, pos_x, pos_y):
        self.agent_x = pos_x
        self.agent_y = pos_y

    def draw(self, win):
        """
        Draw a circle in win.
        """
        center = Point((self.agent_y + 0.5) * GRID_WIDTH, (self.agent_x + 0.5) * GRID_WIDTH)
        radius = GRID_WIDTH / 3
        self.agent = Circle(center, radius)
        color = COLOR[random.randint(0, len(COLOR)-1)]
        COLOR.remove(color)
        self.agent.setFill(color)
        self.agent.draw(win)

    def move(self, new_agent_x, new_agent_y):
        """
        Move to (new_agent_x, new_agent_y)
        """
        dy = (new_agent_x - self.agent_x) * GRID_WIDTH
        self.agent_x = new_agent_x
        dx = (new_agent_y - self.agent_y) * GRID_WIDTH
        self.agent_y = new_agent_y
        self.agent.move(dx, dy)


class GridWorld:
    """
    The whole 2D-grid world with a grid map and some agents.
    """
    def __init__(self, win, grid_map, agent_pos_list):
        self.win = win
        self.grid_map = grid_map
        self.agent_list = list()
        for pos in agent_pos_list:
            self.agent_list.append(Agent(pos[0], pos[1]))
        self.__draw_map()
        self.__draw_agent()

    def __draw_grid(self, pos_x, pos_y, value):
        """
        Draw one grid at (pos_x, pos_y) on map, black if it's a block, white otherwise.
        """
        left_corner = Point(pos_y * GRID_WIDTH, pos_x * GRID_WIDTH)
        right_corner = Point(pos_y * GRID_WIDTH + GRID_WIDTH, pos_x * GRID_WIDTH + GRID_WIDTH)
        grid = Rectangle(left_corner, right_corner)
        if value == 1:
            grid.setFill("black")
        else:
            grid.setFill("white")
        grid.draw(self.win)
        return grid

    def __draw_map(self):
        """
        Draw whole map.
        """
        self.grid_list = list()
        for i, row in enumerate(self.grid_map):
            self.grid_list.append([])
            for j, value in enumerate(row):
                self.grid_list[-1].append(self.__draw_grid(i, j, value))

    def __draw_agent(self):
        """
        Draw every agent.
        """
        for agent in self.agent_list:
            agent.draw(self.win)

    def update(self):
        """
        Update map at random position (pos_x, pos_y) and random color (black/white).
        """
        pos_x = random.randint(0, len(self.grid_map)-1)
        pos_y = random.randint(0, len(self.grid_map[pos_x])-1)
        agent_pos_list = [(agent.agent_x, agent.agent_y) for agent in self.agent_list]
        if (pos_x, pos_y) not in agent_pos_list:
            if self.grid_map[pos_x][pos_y] == 0:
                self.grid_map[pos_x][pos_y] = 1
                self.grid_list[pos_x][pos_y].setFill("black")
            else:
                self.grid_map[pos_x][pos_y] = 0
                self.grid_list[pos_x][pos_y].setFill("white")

    def animate(self):
        """
        Simulate 2-D grid world.
        """
        if random.random() > 0.9:       # change map at random
            self.update()
        for agent in self.agent_list:   # move agent one by one
            new_agent_x, new_agent_y = run(self.grid_map, agent, self.agent_list)
            agent.move(new_agent_x, new_agent_y)
        self.win.after(1000, self.animate)


def is_in_map(grid_map, pos_x, pos_y):
    """
    Check if (pos_x, pos_y) is in grid_map.
    """
    if pos_x < 0 or pos_y < 0:
        return False
    size_x = len(grid_map)
    if pos_x >= size_x:
        return False
    size_y = len(grid_map[pos_x])
    if pos_y >= size_y:
        return False
    return True


def is_not_a_agent(pos_x, pos_y, agent_list):
    """
    Check (pos_x, pos_y) is an agent.
    """
    for agent in agent_list:
        if pos_x == agent.agent_x and pos_y == agent.agent_y:
            return False
    return True


def run(grid_map, agent, agent_list):
    """
    Agent moves one step.
    """
    agent_x = agent.agent_x
    agent_y = agent.agent_y

    s1 = 1
    if is_in_map(grid_map, agent_x-1, agent_y-1) and is_not_a_agent(agent_x-1, agent_y-1, agent_list):
        s1 = grid_map[agent_x-1][agent_y-1]

    s2 = 1
    if is_in_map(grid_map, agent_x-1, agent_y) and is_not_a_agent(agent_x-1, agent_y, agent_list):
        s2 = grid_map[agent_x-1][agent_y]

    s3 = 1
    if is_in_map(grid_map, agent_x-1, agent_y+1) and is_not_a_agent(agent_x-1, agent_y+1, agent_list):
        s3 = grid_map[agent_x-1][agent_y+1]

    s4 = 1
    if is_in_map(grid_map, agent_x, agent_y+1) and is_not_a_agent(agent_x, agent_y+1, agent_list):
        s4 = grid_map[agent_x][agent_y+1]

    s5 = 1
    if is_in_map(grid_map, agent_x+1, agent_y+1) and is_not_a_agent(agent_x+1, agent_y+1, agent_list):
        s5 = grid_map[agent_x+1][agent_y+1]

    s6 = 1
    if is_in_map(grid_map, agent_x+1, agent_y) and is_not_a_agent(agent_x+1, agent_y, agent_list):
        s6 = grid_map[agent_x+1][agent_y]

    s7 = 1
    if is_in_map(grid_map, agent_x+1, agent_y-1) and is_not_a_agent(agent_x+1, agent_y-1, agent_list):
        s7 = grid_map[agent_x+1][agent_y-1]

    s8 = 1
    if is_in_map(grid_map, agent_x, agent_y-1) and is_not_a_agent(agent_x, agent_y-1, agent_list):
        s8 = grid_map[agent_x][agent_y-1]

    x1 = 1 if (s2 == 1 or s3 == 1) else 0
    x2 = 1 if (s4 == 1 or s5 == 1) else 0
    x3 = 1 if (s6 == 1 or s7 == 1) else 0
    x4 = 1 if (s8 == 1 or s1 == 1) else 0

    if x1 == 1 and x2 == 0:
        return agent_x, agent_y+1
    elif x2 == 1 and x3 == 0:
        return agent_x+1, agent_y
    elif x3 == 1 and x4 == 0:
        return agent_x, agent_y-1
    elif x4 == 1 and x1 == 0:
        return agent_x-1, agent_y
    else:
        if is_in_map(grid_map, agent_x-1, agent_y) and is_not_a_agent(agent_x-1, agent_y, agent_list) \
                and grid_map[agent_x-1][agent_y] == 0:
            return agent_x-1, agent_y
        else:
            return agent_x, agent_y


win = GraphWin("Agent", 500, 500)
grid_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
agent_pos_list = [(0, 4), (2, 6)]
world = GridWorld(win, grid_map, agent_pos_list)
world.animate()
world.win.mainloop()
