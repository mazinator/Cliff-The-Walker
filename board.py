import numpy as np
import tkinter as tk
import os

"""
CliffBoard is a class to init and represent a board state
a board is a 12x4 grid, e.g.

* * * * * * * * * * * *
* * * * * * * * * * * *
* * * * * * * * * * * *
x - - - - - - - - - - t

where:
* is an empty field
x is the current position
- is a cliff
t is the target

Rewards:
t = 10
- = -100

Normal step cost is -1 to encourage fast solving
"""


class CliffBoard():

    # Empty board at the beginning
    # Per default, start bottom left and target bottom right
    # 0: normal field
    # 1: start
    # 2: end
    # 3: cliff
    def __init__(self, rows=4, cols=12):
        self.agent_pos = None
        self.board = None
        self.moves = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}
        self.rows = rows
        self.cols = cols
        self.reset()

    def reset(self):
        self.board = np.zeros((self.rows, self.cols))
        self.board[self.rows - 1, 0] = 1  # start position
        self.board[self.rows - 1, 1:self.cols - 1] = 3  # cliff
        self.board[self.rows - 1, self.cols - 1] = 2  # end position
        self.agent_pos = [self.rows - 1, 0]  # agent starts at the bottom-left
        return self.get_state()  # return initial state

    def get_state(self):
        return tuple(self.agent_pos)

    def print_board(self):
        os.system('clear')  # Clear the console first
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r, c] == 0:
                    print('*', end=' ')
                elif self.board[r, c] == 1:
                    print('x', end=' ')  # start position
                elif self.board[r, c] == 2:
                    print('t', end=' ')  # target position
                elif self.board[r, c] == 3:
                    print('-', end=' ')  # cliff
            print()  # Move to the next line after printing each row

    def make_move(self, move: str):
        """
        Makes a move on the board, returns .

        @:param
        move: UP, DOWN, LEFT, RIGHT (1 to 4)

        @:returns
        board-state, reward, finished
        """

        # check if valid move
        if move not in self.moves:
            raise ValueError("Invalid move. Use 'UP', 'DOWN', 'LEFT', or 'RIGHT'.")

        # set new row/col given the move
        new_row = self.agent_pos[0] + self.moves[move][0]
        new_col = self.agent_pos[1] + self.moves[move][1]

        # check if move results in bumping to a wall
        if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
            return self.get_state(), -1, False

        # reset agents position on board
        self.board[self.agent_pos[0], self.agent_pos[1]] = 0
        self.agent_pos = [new_row, new_col]
        self.board[self.agent_pos[0], self.agent_pos[1]] = 1

        # check if new position is a cliff
        # if yes, put agent to the beginning and make reward -100
        if self.board[new_row, new_col] == 3:
            self.agent_pos = [self.rows - 1, 0]
            return self.get_state(), -100, False

        # check if game completed
        # if yes, return reward 10 and mark game as finished
        if self.board[new_row, new_col] == 2:
            return self.get_state(), 10, True

        # otherwise, return reward -1
        return self.get_state(), -1, False




