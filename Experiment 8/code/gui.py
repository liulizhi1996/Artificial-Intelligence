from graphics import *
import re
from maximin import alpha_beta
import os


class Board:
    def __init__(self):
        self.win = GraphWin("Gomoku", 1000, 800)
        self.current = 1      # current player 1 - black, 2 - white
        self.current_point = None
        self.composition = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]
        self.turn_black_circle = Circle(Point(810, 300), 20)
        self.turn_black_circle.setFill("black")
        self.turn_black_circle.setOutline("black")
        self.turn_white_circle = Circle(Point(810, 400), 20)
        self.turn_white_circle.setFill("white")
        self.turn_white_circle.setOutline("white")
        self.draw()

    def draw(self):
        self.win.setBackground("orange")
        for i in range(1, 16):
            line = Line(Point(50 * i, 50), Point(50 * i, 50 * 15))
            line.setWidth(2)
            line.draw(self.win)
            label = Text(Point(50 * i, 20), chr(ord('A') + i - 1))
            label.setSize(12)
            label.draw(self.win)
            line = Line(Point(50, 50 * i), Point(50 * 15, 50 * i))
            line.setWidth(2)
            line.draw(self.win)
            label = Text(Point(20, 50 * i), str(i))
            label.setSize(12)
            label.draw(self.win)
        circle = Circle(Point(4 * 50, 4 * 50), 5)
        circle.setFill("black")
        circle.draw(self.win)
        circle = Circle(Point(12 * 50, 4 * 50), 5)
        circle.setFill("black")
        circle.draw(self.win)
        circle = Circle(Point(4 * 50, 12 * 50), 5)
        circle.setFill("black")
        circle.draw(self.win)
        circle = Circle(Point(12 * 50, 12 * 50), 5)
        circle.setFill("black")
        circle.draw(self.win)
        circle = Circle(Point(8 * 50, 8 * 50), 5)
        circle.setFill("black")
        circle.draw(self.win)
        if self.current == 1:
            self.turn_black_circle.draw(self.win)
        else:
            self.turn_white_circle.draw(self.win)
        turn_black_msg = Text(Point(880, 300), "BLACK")
        turn_black_msg.setSize(24)
        turn_black_msg.setFace("arial")
        turn_black_msg.setStyle("bold")
        turn_black_msg.draw(self.win)
        turn_white_msg = Text(Point(880, 400), "WHITE")
        turn_white_msg.setSize(24)
        turn_white_msg.setFace("arial")
        turn_white_msg.setStyle("bold")
        turn_white_msg.draw(self.win)

    def put_chess(self, pos_x, pos_y):
        chess = Circle(Point(pos_y * 50, pos_x * 50), 20)
        self.composition[pos_x - 1][pos_y - 1] = str(self.current)
        if self.current == 1:
            chess.setOutline("black")
            chess.setFill("black")
        else:
            chess.setOutline("white")
            chess.setFill("white")
        chess.draw(self.win)
        if self.current_point:
            self.current_point.undraw()
        self.current_point = Circle(Point(pos_y * 50, pos_x * 50), 2)
        self.current_point.setFill("red")
        self.current_point.setOutline("red")
        self.current_point.draw(self.win)

    def is_finished(self, pos_x, pos_y):
        horizon = ''.join(self.composition[pos_x - 1])
        m = re.search(r'%d{5}' % self.current, horizon)
        if m:
            return True
        vertical = ''.join([self.composition[i][pos_y - 1] for i in range(15)])
        m = re.search(r'%d{5}' % self.current, vertical)
        if m:
            return True
        main_diagonal = ''.join([self.composition[pos_x + i][pos_y + i]
                                for i in range(max([-pos_x, -pos_y]), min([14 - pos_x, 14 - pos_y]) + 1)])
        m = re.search(r'%d{5}' % self.current, main_diagonal)
        if m:
            return True
        anti_diagonal = ''.join([self.composition[pos_x - 1 + i][pos_y - 1 - i]
                                for i in range(max([-pos_x+1, -15 + pos_y]), min([15 - pos_x, pos_y-1]) + 1)])
        m = re.search(r'%d{5}' % self.current, anti_diagonal)
        if m:
            return True

    def play(self):
        while True:
            if self.current == 1:
                click_point = self.win.getMouse()
                point_x = int(click_point.getY())
                shift = (point_x + 10) % 50
                pos_x = (point_x + 10) // 50 if shift <= 20 else -1
                point_y = int(click_point.getX())
                shift = (point_y + 10) % 50
                pos_y = (point_y + 10) // 50 if shift <= 20 else -1
                if not 1 <= pos_x <= 15 or not 1 <= pos_y <= 15:
                    continue
            else:
                v, choice = alpha_beta(self.composition, 0, 0, 1, -float('inf'), float('inf'), self.current, self.current)
                pos_x, pos_y = choice[0], choice[1]
            if pos_x and pos_y and self.composition[pos_x - 1][pos_y - 1] == '0':
                self.put_chess(pos_x, pos_y)
                if self.is_finished(pos_x, pos_y):
                    text = "%s WINS!" % ("BLACK" if self.current == 1 else "WHITE")
                    win_msg = Text(Point(875, 500), text)
                    win_msg.setStyle("bold")
                    win_msg.setFace("arial")
                    win_msg.setTextColor("red")
                    win_msg.setSize(24)
                    win_msg.draw(self.win)
                    # only support on MAC OS X
                    if self.current == 1:
                        os.system('say --voice="Good News" Wo Congratulations! You defeat A I!')
                    else:
                        os.system('say --voice="Bad News" Ha Ha Ha You are loser! No one can defeat me!')
                    break
                if self.current == 1:
                    self.current = 2
                    self.turn_black_circle.undraw()
                    self.turn_white_circle.draw(self.win)
                else:
                    self.current = 1
                    self.turn_white_circle.undraw()
                    self.turn_black_circle.draw(self.win)


if __name__ == "__main__":
    while True:
        board = Board()
        board.play()
        board.win.getMouse()
        board.win.close()
    board.win.mainloop()
