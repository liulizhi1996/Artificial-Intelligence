from tkinter import *
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText
import bfs
import dfs
import iddfs
import bidirectional
import auxiliary


def get_initial_state():
    hash_map = dict([(str(num), False) for num in range(9)])
    entry_list = [initial_board_input11, initial_board_input12, initial_board_input13,
                  initial_board_input21, initial_board_input22, initial_board_input23,
                  initial_board_input31, initial_board_input32, initial_board_input33]
    block_list = list()
    for entry in entry_list:
        block = entry.get() if (len(entry.get()) == 1) else '0'
        if block in hash_map and not hash_map[block]:
            hash_map[block] = True
            block_list.append(int(block))
        else:
            return False
    board = ((block_list[0], block_list[1], block_list[2]),
             (block_list[3], block_list[4], block_list[5]),
             (block_list[6], block_list[7], block_list[8]))
    return board


def get_goal_state():
    hash_map = dict([(str(num), False) for num in range(9)])
    entry_list = [goal_board_input11, goal_board_input12, goal_board_input13,
                  goal_board_input21, goal_board_input22, goal_board_input23,
                  goal_board_input31, goal_board_input32, goal_board_input33]
    block_list = list()
    for entry in entry_list:
        block = entry.get() if (len(entry.get()) == 1) else '0'
        if block in hash_map and not hash_map[block]:
            hash_map[block] = True
            block_list.append(int(block))
        else:
            return False
    board = ((block_list[0], block_list[1], block_list[2]),
             (block_list[3], block_list[4], block_list[5]),
             (block_list[6], block_list[7], block_list[8]))
    return board


def solve():
    initial_state = get_initial_state()
    if not initial_state:
        tkinter.messagebox.showerror('错误', '非法初始状态')
        return
    goal_state = get_goal_state()
    if not goal_state:
        tkinter.messagebox.showerror('错误', '非法目标状态')
        return
    choice = var.get()
    path = []
    if choice == 1:
        path = bfs.breadth_first_search(initial_state, goal_state)
    elif choice == 2:
        path = dfs.depth_first_search(initial_state, goal_state)
    elif choice == 3:
        path = iddfs.iterative_deepening_dfs(initial_state, goal_state)
    elif choice == 4:
        path = bidirectional.bidirectional_search(initial_state, goal_state)
    output.delete(1.0, END)
    output.insert(1.0, auxiliary.path_to_str(path))


root = Tk(className=" Eight Puzzle ")

win = Canvas(root, width=800, height=700, background="white")
win.pack()

# initial board
win.create_rectangle(50, 50, 350, 350, width=4)
# initial board title
win.create_text(200, 25, text="Initial State", font=tkFont.Font(family="arial", size=18, weight=tkFont.BOLD))
# horizon line 1
win.create_line(50, 150, 350, 150, width=4)
# horizon line 2
win.create_line(50, 250, 350, 250, width=4)
# vertical line 1
win.create_line(150, 50, 150, 350, width=4)
# vertical line 2
win.create_line(250, 50, 250, 350, width=4)
# entry at (1, 1)
initial_board_input11 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input11.place(height=50, width=50, x=75, y=75)
initial_board_input11.insert(0, '2')
# entry at (1, 2)
initial_board_input12 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input12.place(height=50, width=50, x=175, y=75)
initial_board_input12.insert(0, '8')
# entry at (1, 3)
initial_board_input13 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input13.place(height=50, width=50, x=275, y=75)
initial_board_input13.insert(0, '1')
# entry at (2, 1)
initial_board_input21 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input21.place(height=50, width=50, x=75, y=175)
initial_board_input21.insert(0, '4')
# entry at (2, 2)
initial_board_input22 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input22.place(height=50, width=50, x=175, y=175)
initial_board_input22.insert(0, '6')
# entry at (2, 3)
initial_board_input23 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input23.place(height=50, width=50, x=275, y=175)
initial_board_input23.insert(0, '3')
# entry at (3, 1)
initial_board_input31 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input31.place(height=50, width=50, x=75, y=275)
initial_board_input31.insert(0, '')
# entry at (3, 2)
initial_board_input32 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input32.place(height=50, width=50, x=175, y=275)
initial_board_input32.insert(0, '7')
# entry at (3, 3)
initial_board_input33 = Entry(root, bg="White", bd=0,
                              font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
initial_board_input33.place(height=50, width=50, x=275, y=275)
initial_board_input33.insert(0, '5')


# goal board
win.create_rectangle(450, 50, 750, 350, width=4)
# goal board title
win.create_text(600, 25, text="Goal State", font=tkFont.Font(family="arial", size=18, weight=tkFont.BOLD))
# horizon line 1
win.create_line(450, 150, 750, 150, width=4)
# horizon line 2
win.create_line(450, 250, 750, 250, width=4)
# vertical line 1
win.create_line(550, 50, 550, 350, width=4)
# vertical line 2
win.create_line(650, 50, 650, 350, width=4)
# entry at (1, 1)
goal_board_input11 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input11.place(height=50, width=50, x=475, y=75)
goal_board_input11.insert(0, '1')
# entry at (1, 2)
goal_board_input12 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input12.place(height=50, width=50, x=575, y=75)
goal_board_input12.insert(0, '2')
# entry at (1, 3)
goal_board_input13 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input13.place(height=50, width=50, x=675, y=75)
goal_board_input13.insert(0, '3')
# entry at (2, 1)
goal_board_input21 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input21.place(height=50, width=50, x=475, y=175)
goal_board_input21.insert(0, '8')
# entry at (2, 2)
goal_board_input22 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input22.place(height=50, width=50, x=575, y=175)
goal_board_input22.insert(0, '')
# entry at (2, 3)
goal_board_input23 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input23.place(height=50, width=50, x=675, y=175)
goal_board_input23.insert(0, '4')
# entry at (3, 1)
goal_board_input31 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input31.place(height=50, width=50, x=475, y=275)
goal_board_input31.insert(0, '7')
# entry at (3, 2)
goal_board_input32 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input32.place(height=50, width=50, x=575, y=275)
goal_board_input32.insert(0, '6')
# entry at (3, 3)
goal_board_input33 = Entry(root, bg="White", bd=0,
                           font=tkFont.Font(family="arial", size=32, weight=tkFont.BOLD), justify="center")
goal_board_input33.place(height=50, width=50, x=675, y=275)
goal_board_input33.insert(0, '5')


# choose search algorithm
var = IntVar()
# bfs: 1
bfs_button = Radiobutton(root, text="Breadth First Search", variable=var, value=1)
bfs_button.place(x=25, y=370)
bfs_button.select()
# dfs: 2
dfs_button = Radiobutton(root, text="Depth First Search", variable=var, value=2)
dfs_button.place(x=195, y=370)
# iddfs: 3
iddfs_button = Radiobutton(root, text="Iterative Deepening Depth First Search", variable=var, value=3)
iddfs_button.place(x=355, y=370)
# bidir: 4
bidir_button = Radiobutton(root, text="Bidirectional Search", variable=var, value=4)
bidir_button.place(x=625, y=370)


# result output
output = ScrolledText(root, width=30, height=15, bg="Gray", wrap=WORD)
output.place(x=300, y=450)


# solve button
solve_button = Button(root, text="solve", bg="Gray", bd=5, justify="center", command=solve,
                      font=tkFont.Font(family="arial", size=18, weight=tkFont.BOLD))
solve_button.place(x=365, y=405)

mainloop()
