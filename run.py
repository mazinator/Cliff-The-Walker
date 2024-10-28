from board import *
import time


def main():
    board = CliffBoard()

    board.print_board()

    """for i in range(1, 10):
        time.sleep(0.5)
        board.make_move('UP')
        board.print_board()

    for i in range(1, 20):
        time.sleep(0.1)
        board.make_move('RIGHT')
        board.print_board()

    for i in range(1, 20):
        time.sleep(0.1)
        board.make_move('DOWN')
        board.print_board()"""



if __name__ == '__main__':
    main()
