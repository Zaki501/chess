import numpy as np


def test():
    """convert list of dicts to numpy 8x8 array"""
    board = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(8):
        [board.append({(char + str(i + 1)): "x"}) for char in letters]
    numpy_board = np.asarray(board)
    numpy_board.shape = (8, 8)
    return numpy_board


def init_board():
    """adds starting position to the board"""
    # input key value board, change values and output


def place_piece(board, piece, position):
    """Place a piece at a position"""
    next((piece for piece in board if piece["user"] == "unknown user"), "Nothing found")


def find_piece(board):
    return next(
        (piece for piece in board if next(iter(piece)) == "A1"), "Nothing found"
    )


def for_loop(board):
    for row in board:
        for position in row:
            for key, value in position.items():
                # print(key, value)
                # print(value)
                if key == "B2":
                    print("test")
                item_index = np.where(board == position)
                print(item_index)
    print(board)


def main():
    np.set_printoptions(linewidth=1000)  # increase terminal width
    board = test()
    # # print(board)
    # # print(enumerate(board))
    # numpy_board = test()
    # x = {"day": "saturday"}
    # print(next(iter(x)))

    # methods = [method_name for method_name in dir(board)
    #            if callable(getattr(board, method_name))]
    # print(methods)
    # print(board)
    # print(find_piece(board))
    # print(board.tolist.index({'C1': 'x'}))
    # print(dir(board))
    for_loop(board)


if __name__ == "__main__":
    main()
