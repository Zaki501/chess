import numpy as np


def empty_board():
    """Returns empty 8x8 board"""
    return np.empty(shape=(8, 8), dtype=object)


def new_board():
    """create an 8x8 board with chess positions"""
    board = empty_board()
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(8):
        board[i] = [{(str(i) + char): ""} for char in letters]
    return board


def main():
    test = new_board()
    print(test)


if __name__ == "__main__":
    np.set_printoptions(linewidth=1000)  # increase terminal width
    main()
