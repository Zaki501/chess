# an 8x8 board that contains the position, index, and piece
# converts to "display", which shows pieces on a board for the user (white and black POV)
import numpy as np


def empty_board():
    """Returns empty 8x8 board"""
    return np.empty(shape=(8, 8), dtype=object)


def init_board():
    """fill an 8x8 board with chess positions"""
    board = empty_board()
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(8):
        board[i] = [{(char + str(i + 1)): ""} for char in letters]
    return board


def place_piece(board, current_position, new_position):
    """Move piece from one index to another"""
    # first get the current position


def move_piece():
    """find piece, and move it

    Is it valid move? if so, is there another piece there? Can that piece be captured?"""


def main():
    board = init_board()
    print(board)
    return board


if __name__ == "__main__":
    np.set_printoptions(linewidth=1000)  # increase terminal width
    main()
