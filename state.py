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
    for idx, item in np.ndenumerate(board):
        item.update({"index": idx})
    return board


def place_piece(board, current_position, new_position):
    """Move piece from one index to another"""
    # first get the current position


def find_piece(board, piece):
    """find a piece, and return it"""
    print("LOOPING")
    for row in board:
        for position in row:
            for key, value in position.items():
                if key == piece:
                    # print("test")
                    # item_index = np.where(board == position)
                    # print(item_index)
                    print(key, value)
    return piece


def move_piece():
    """find piece, and move it

    Is it valid move? if so, is there another piece there? Can that piece be captured?"""


def test():
    # convert an array to list, then back to array
    a = list(range(4))
    b = np.asarray(a).reshape((2, 2))
    # t = np.arange(4)
    c = b.tolist()
    print("a", a)
    print(b)
    print(c)
    print(c[1][1])


def pieces_on_board(board):
    """take the pieces out of the board, and display them"""


def main():
    # # narray to list : .tolist()
    # # list to narray: np.asarray(list, datatype)

    # full_board = init_board()
    # print(full_board)
    # # for idx, item in np.ndenumerate(full_board):
    # #     print(item)
    # keys = np.fromiter(full_board.keys(), dtype=float)
    # print(keys)
    print("main")


if __name__ == "__main__":
    np.set_printoptions(linewidth=1000)  # increase terminal width
    main()
