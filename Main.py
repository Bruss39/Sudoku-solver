from math import sqrt
from time import time

# --- SETTINGS ---
sudoku_number = 4  # 0, 1 ...

# --- PROBLEMS & SOLUTIONS ---
boards = [
    [
        [4, 1, 2, 0],
        [0, 2, 0, 4],
        [1, 4, 0, 2],
        [2, 3, 4, 1],
    ],
    [
        [0, 1, 4, 0],
        [0, 4, 0, 1],
        [0, 3, 0, 2],
        [0, 0, 0, 0],
    ],
    [
        [3, 8, 6, 0, 0, 0, 2, 4, 5],
        [0, 2, 0, 3, 5, 6, 8, 0, 0],
        [0, 7, 0, 0, 8, 0, 0, 1, 0],
        [0, 0, 0, 0, 6, 4, 9, 8, 7],
        [0, 4, 0, 7, 3, 0, 0, 6, 0],
        [1, 0, 7, 2, 0, 0, 0, 5, 4],
        [7, 0, 0, 0, 4, 1, 5, 2, 0],
        [0, 0, 2, 5, 7, 0, 4, 0, 8],
        [0, 5, 0, 6, 2, 9, 7, 0, 0],
    ],
    [
        [0, 0, 0, 0, 8, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 1, 6, 2, 0],
        [0, 9, 2, 0, 0, 6, 4, 7, 0],
        [6, 0, 0, 1, 0, 0, 0, 9, 0],
        [4, 5, 0, 0, 3, 0, 0, 6, 1],
        [0, 1, 0, 0, 0, 5, 0, 0, 7],
        [0, 8, 7, 4, 0, 0, 1, 3, 0],
        [0, 2, 6, 8, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 6, 0, 0, 0, 0],
    ],
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    [
        [7, 0, 0, 0, 8, 3, 0, 0, 0],
        [9, 0, 2, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 5, 2],
        [8, 0, 6, 0, 0, 0, 1, 0, 0],
        [4, 0, 0, 8, 0, 1, 0, 0, 7],
        [0, 0, 1, 0, 0, 0, 2, 0, 4],
        [3, 6, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 8, 0, 6],
        [0, 0, 0, 5, 7, 0, 0, 0, 3]
    ],
    [
        [ 3, 13,  0,  0, 15,  0,  0,  0,  0,  7,  6,  4,  0, 16,  0, 14],
        [ 0,  0,  0,  2, 11,  0, 13,  8,  0,  0,  0,  0,  5, 10,  0,  3],
        [ 0,  0,  0, 14,  9,  0, 16,  4,  0,  0,  2, 15,  0,  6,  0,  0],
        [ 0, 11,  7, 10,  0,  0,  6,  0,  9,  0,  0, 13,  0,  4, 12,  0],
        [ 0,  2, 15,  0,  0, 16,  0,  0,  0,  6, 10,  9,  0,  0,  0,  0],
        [ 0,  0, 16,  0,  5,  8,  0, 15, 13,  3,  0,  0, 12,  0, 11, 10],
        [ 7,  5,  0,  0,  0,  0, 10,  0,  0,  0,  8,  1,  6, 15, 16,  0],
        [ 1, 10,  8,  0, 13,  6,  4,  0,  0,  0,  0,  0,  0,  0,  3,  9],
        [11, 16,  0,  0,  0,  0,  0,  0,  0, 12,  9,  7,  0,  1, 10, 15],
        [ 0,  1, 10, 15,  7, 13,  0,  0,  0,  2,  0,  0,  0,  0,  6, 12],
        [ 9,  3,  0,  7,  0,  0, 15,  6,  5,  0, 16,  8,  0, 11,  0,  0],
        [ 0,  0,  0,  0,  3, 11,  8,  0,  0,  0, 15,  0,  0,  9,  7,  0],
        [ 0,  7,  5,  0,  6,  0,  0, 12,  0,  4,  0,  0,  9,  2, 14,  0],
        [ 0,  0,  3,  0,  4, 10,  0,  0, 16,  5,  0,  6,  1,  0,  0,  0],
        [ 6,  0, 11, 13,  0,  0,  0,  0,  2,  9,  0, 12, 10,  0,  0,  0],
        [12,  0,  4,  0, 16,  9,  7,  0,  0,  0,  0, 10,  0,  0,  5,  6]
    ]
]


def print_board(board):
    """
    Simply print a sudoku board
    """
    for row in board:
        print("  ".join(map(str, row)))


def find_empty_location(board):
    """
    Locate the first empty position on the tab.

    Parameters:
    - board: A list of lists representing the Sudoku board.

    Returns:
    The position of the first empty position, otherwise None, None.
    """
    for row in board:
        for num in row:
            if num == 0:
                return row.index(num), board.index(row)
    return None, None


def backtracking_method(board):
    """
    The function finds whether a number can be positioned within a column, a row and a square.
    If the answer is yes, it repeats the cycle for the rest of the empty cells.
    If he can't solve the sudoku, he goes back to the last modified cell and overwrites it with another number.
    The cycle is repeated until the sudoku is completed or no solution has been found.

    Parameters:
    - board: A list of lists representing the Sudoku board.

    Returns:
    True if the Sudoku card was solved successfully, False otherwise.
    """
    x, y = find_empty_location(board)

    # If there are no more empty cells, the loop ends
    if x is None and y is None:
        return True

    # It tries to enter the first valid number.
    for num in range(1, len(board[0]) + 1):
        if is_valid(board, y, x, num):
            boards[sudoku_number][y][x] = num

            # It tries to solve the remaining part of the Sudoku by starting the cycle again.
            if backtracking_method(board):
                return True

            # Cancel the assignment if the previous number was incorrect.
            board[y][x] = 0

    # No solution found for this sudoku
    return False


def is_valid(board, row, col, num):
    """
    It checks that the subject number is not present in the row, column, and current square.

    Parameters:
    - board: A list of lists representing the Sudoku board.
    - row: Row (x) used for the validation of the number 'num'.
    - column: Column (y) used for the validation of the number 'num'.
    - num: Number subject to validation.

    Returns:
    The function returns True if the number is valid for the specified position, and False otherwise.
    """
    square_size = int(sqrt(len(board[0])))

    # Check if the number is present in the same row or column.
    if any(board[row][i] == num or board[i][col] == num for i in range(square_size * square_size)):
        return False

    # Check if the number is present in the same subgrid.
    start_row, start_col = square_size * (row // square_size), square_size * (col // square_size)
    if any(
            board[start_row + i][start_col + j] == num
            for i in range(square_size)
            for j in range(square_size)
    ):
        return False

    return True


def find_pinned_num_position(board):
    empty_positions = []
    for row in board:
        for col in row:
            if type(col) != int:
                empty_positions.append([row.index(col), board.index(row)])  # x, y
    return empty_positions


def pinned_num_method(board):
    while True:
        old_board = [row[:] for row in board]

        Cell.assign_pinned_number(board)
        Cell.remove_already_present(board)

        if old_board == board:
            break



class Cell:
    def __init__(self, board: list):
        self.pinned_number = []
        for n in range(1, len(board[0]) + 1):
            self.pinned_number.append(n)

    def __repr__(self):
        return str(self.pinned_number)

    @staticmethod
    def assign_pinned_number(board):
        while True:
            x, y = find_empty_location(board)
            if x is None:
                break
            board[y][x] = Cell(board)

    @staticmethod
    def remove_already_present(board):
        empty_positions = find_pinned_num_position(board)
        for pos in empty_positions:
            x, y = pos

            for n in range(1, len(board[0]) + 1):
                if not is_valid(board, y, x, n):
                    if n in board[y][x].pinned_number:
                        board[y][x].pinned_number.remove(n)
                        if len(board[y][x].pinned_number) == 1:
                            board[y][x] = board[y][x].pinned_number[0]
                            print(f"Found {board[y][x]} in x:{x}, y:{y}")
                            break

        if len(find_pinned_num_position(board)) == 0:
            return True
        else:
            for pos in find_pinned_num_position(board):
                x, y = pos
                board[y][x] = 0
            return False


if __name__ == "__main__":
    sudoku_board = boards[sudoku_number]
    print("Sudoku:")
    print_board(sudoku_board)

    start = time()  # start stopwatch
    pinned_num_method(sudoku_board)

    if backtracking_method(sudoku_board):
        timer = time() - start  # stop stopwatch
        print(f"\nResolved in {timer} sec:")
        print_board(boards[sudoku_number])
    else:
        print("Sudoku has no solution.")

    input("\nPress Enter to exit...")
