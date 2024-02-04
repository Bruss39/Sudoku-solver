import math, time

# --- SETTINGS ---
problem_number = 0  # 0, 1 ...
max_attempts = 3

# --- PROBLEMS & SOLUTIONS ---
problems = [
    [
        [0, 3, 1, 0],
        [0, 0, 0, 0],
        [3, 1, 0, 2],
        [4, 0, 3, 1]
    ],
    [
        [3, 0, 0, 7, 0, 8, 0, 1, 0],
        [0, 6, 0, 0, 3, 5, 0, 0, 2],
        [0, 0, 5, 6, 0, 0, 8, 3, 9],
        [1, 0, 2, 0, 0, 0, 0, 7, 0],
        [0, 8, 0, 0, 0, 0, 0, 6, 0],
        [0, 3, 0, 0, 0, 0, 4, 0, 5],
        [9, 1, 7, 0, 0, 4, 6, 0, 0],
        [4, 0, 0, 8, 6, 0, 0, 5, 0],
        [0, 5, 0, 2, 0, 7, 0, 0, 4]
    ]
]

solutions = [
    [
        [2, 3, 1, 4],
        [1, 4, 2, 3],
        [3, 1, 4, 2],
        [4, 2, 3, 1]
    ],
    [
        [3, 9, 4, 7, 2, 8, 5, 1, 6],
        [8, 6, 1, 9, 3, 5, 7, 4, 2],
        [2, 7, 5, 6, 4, 1, 8, 3, 9],
        [1, 4, 2, 5, 8, 6, 9, 7, 3],
        [5, 8, 9, 4, 7, 3, 2, 6, 1],
        [7, 3, 6, 1, 9, 2, 4, 8, 5],
        [9, 1, 7, 3, 5, 4, 6, 2, 8],
        [4, 2, 3, 8, 6, 9, 1, 5, 7],
        [6, 5, 8, 2, 1, 7, 3, 9, 4]
    ]
]

range_of_possible_num = None  # do not change me
to_check = solutions[problem_number]


def solver():
    attempts = 0
    empty_pos = []
    line_array_, column_array_, squares_array_ = update_data()
    while 1:
        empty_qty, empty_pos, squares = find_empty_pos(empty_pos)
        old_empty_qty = empty_qty
        if empty_qty == old_empty_qty:
            attempts += 1
            if attempts == 3:
                return False
        if empty_qty == 0:
            return True
        else:
            range_of_possible_number = int(range_of_possible_num)

            # # ---------------------  ONE EMPTY CELL  ------------------------

            # for square in squares_array_:
            #     for num in range(1, range_of_possible_number + 1):
            #         free_cell_square = square.count(0)
            #         if num not in square:
            #             if free_cell_square == 1:
            #                 for elm in empty_pos:
            #                     if elm[2] == squares_array_.index(square):
            #                         problems[problem_number] = add_new_number(num, elm[1], elm[0])
            #                         del empty_pos[empty_pos.index(elm)]
            # line_array_, column_array_, squares_array_ = update_data()
            # empty_pos = []
            # empty_qty, empty_pos, squares = find_empty_pos(empty_pos)

            # # ---------------------  ONE EMPTY COLUMN  ------------------------

            # for column in column_array_:
            #     for num in range(1, range_of_possible_number + 1):
            #         free_cell_column = column.count(0)
            #         if num not in column:
            #             if free_cell_column == 1:
            #                 for elm in empty_pos:
            #                     if elm[1] == column_array_.index(column):
            #                         problems[problem_number] = add_new_number(num, elm[1], elm[0])
            #                         del empty_pos[empty_pos.index(elm)]
            # line_array_, column_array_, squares_array_ = update_data()
            # empty_pos = []
            # empty_qty, empty_pos, squares = find_empty_pos(empty_pos)

            # # ---------------------  ONE EMPTY LINE  ------------------------

            # for line in line_array_:
            #     for num in range(1, range_of_possible_number + 1):
            #         free_cell_line = line.count(0)
            #         if num not in line:
            #             if free_cell_line == 1:
            #                 for elm in empty_pos:
            #                     if elm[0] == line_array_.index(line):
            #                         problems[problem_number] = add_new_number(num, elm[1], elm[0])
            #                         del empty_pos[empty_pos.index(elm)]
            # line_array_, column_array_, squares_array_ = update_data()
            # empty_pos = []
            # empty_qty, empty_pos, squares = find_empty_pos(empty_pos)

            # ---------------------  EXCLUSION MODE  ------------------------

            if exlusion_mode(line_array_, column_array_, squares_array_):
                break

            # possible_num = int(range_of_possible_num)
            # num_for_columns_and_rows = int(math.sqrt(possible_num))

            # for square in squares:
            #     for empty_tuple in empty_pos:
            #         if squares.index(square) == empty_tuple[2]:  # verify presence of 0 in the current square
            #             for num in range(1, possible_num + 1):
            #                 rows = [0] * num_for_columns_and_rows
            #                 columns = [0] * num_for_columns_and_rows

            #                 for i in range(0, num_for_columns_and_rows):
            #                     if num in line_array_[i]:
            #                         rows[i] = 1
            #                 for i in range(0, num_for_columns_and_rows):
            #                     if num in column_array_[i]:
            #                         columns[i] = 1

            #                 for cell in square:
            #                     if cell == 0:
            #                         row_index, col_index = empty_tuple[0], empty_tuple[1]
            #                         if rows[row_index] == 0 and columns[col_index] == 0:
            #                             add_new_number(num, [row_index], [col_index])
            #                             print(num)
            #                             print(empty_tuple)
            #                             print(row_index)
            #                             print(col_index)
            #                             print(f"Found {num} in position x:{col_index}, y:{row_index}")


def trova_numero_assente(riga, colonna, blocco):
    possible_num = set(range(1, int(range_of_possible_num)+1))
    possible_num -= set(riga)
    possible_num -= set(colonna)
    possible_num -= set(blocco)
    return list(possible_num)


def exlusion_mode(lines, rows, squares):
    celle_vuote = trova_celle_vuote(problems[problem_number])

    def check():
        if not celle_vuote:
            return True

    check()

    i, j = celle_vuote[0]
    riga = problems[problem_number][i]
    col = [problems[problem_number][x][j] for x in range(int(range_of_possible_num))]
    block = [problems[problem_number][x][y] for x in range(i // 3 * 3, (i // 3 + 1) * 3) for y in range(j // 3 * 3, (j // 3 + 1) * 3)]

    possible_num = trova_numero_assente(riga, col, block)

    for num in possible_num:
        add_new_number(num, j, i)

        check()

        problems[problem_number][i][j] = 0


def check_value(line, column):
    if problems[problem_number][column][line] == to_check[column][line]:
        return True
    else:
        return False


def update_data():      
    line_array_ = problems[problem_number]
    squares_array_ = create_square_array()
    column_array_ = create_column_array()

    return line_array_, column_array_, squares_array_


def print_solution(array_solution, timer=None):
    print(f"\nSolved in {timer} sec:")
    for i in array_solution:
        for j in i:
            print(f"{j}    ", end="")
        print("\n")


def solution_compare(prob, sol):
    if prob == sol:
        print("--> CORRECT!   ;)\n")
    else:
        print("--> ERROR in the algorithm...   :(\n")


def find_empty_pos(pos):
    empty = 0
    squares = create_square_array()
    for i in problems[problem_number]:
        x = 0
        for j in i:
            if j == 0:
                empty += 1
                pos.append(
                    (problems[problem_number].index(i), x,
                     find_square_of_num(problems[problem_number].index(i), x, len(squares))))  # line, column, square
            x += 1
    return empty, pos, squares


def trova_celle_vuote(sudoku):
    celle_vuote = []
    for i in range(int(range_of_possible_num)):
        for j in range(int(range_of_possible_num)):
            if sudoku[i][j] == 0:
                celle_vuote.append((i, j))
    return celle_vuote


def create_square_array():
    array = []
    global range_of_possible_num
    range_of_possible_num = len(problems[problem_number][0])
    # print(f"Type of problems[problem_number]: {range_of_possible_num}x{range_of_possible_num}")
    internal_value = int(math.sqrt(range_of_possible_num))

    for row_start in range(0, len(problems[problem_number]), internal_value):
        for col_start in range(0, len(problems[problem_number][0]), internal_value):
            square = []
            for i in range(internal_value):
                for j in range(internal_value):
                    square.append(problems[problem_number][row_start + i][col_start + j])
            array.append(square)

    return array


def create_column_array():
    num_rows = len(problems[problem_number])
    num_cols = len(problems[problem_number][0])

    column_array = []
    for col in range(num_cols):
        column = [problems[problem_number][row][col] for row in range(num_rows)]
        column_array.append(column)

    return column_array


def find_square_of_num(line, column, num_squares):
    square_size = int(math.sqrt(num_squares))

    square_row = line // square_size
    square_col = column // square_size

    return square_row * square_size + square_col


def add_new_number(number, line, column):
    if type(line) is list and type(column) is list:
        line = line[0]
        column = column[0]
    problems[problem_number][column][line] = number

    print(f"Found {number} in position x:{line}, y:{column} -> {check_value(line, column)}")
    return problems[problem_number]


if __name__ == "__main__":
    start = time.time()
    solution = solver()  # select problem to solve
    end = time.time() - start

    if solution:
        print_solution(problems[problem_number], end)  # print result
        solution_compare(problems[problem_number], solutions[problem_number])  # compare result with the solution
    else:
        print("-->  To attempts failed: unsolvable.  <--")

    input("Press Enter to exit...\n")
