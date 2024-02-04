import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, master, puzzle):
        self.master = master
        self.master.title("Sudoku Solver")

        self.puzzle = puzzle
        self.size = len(puzzle)
        self.range_of_possible_num = self.size

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=360, height=360)
        self.canvas.pack()

        self.draw_grid()
        self.draw_puzzle()

        solve_button = tk.Button(self.master, text="Risoluzione Rapida", command=self.solve_quick)
        solve_button.pack(pady=10)

        solve_step_button = tk.Button(self.master, text="Passo Successivo", command=self.solve_step)
        solve_step_button.pack(pady=10)

    def draw_grid(self):
        for i in range(1, 9):
            line_width = 2 if i % 3 == 0 else 1
            self.canvas.create_line(i * 40, 0, i * 40, 360, width=line_width)
            self.canvas.create_line(0, i * 40, 360, i * 40, width=line_width)

    def draw_puzzle(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] != 0:
                    self.canvas.create_text(j * 40 + 20, i * 40 + 20, text=str(self.puzzle[i][j]))

    def solve_quick(self):
        sudoku_solver = SudokuSolver(self.puzzle)
        if sudoku_solver.solve():
            self.update_canvas()
        else:
            messagebox.showinfo("Errore", "Il Sudoku non è risolvibile.")

    def solve_step(self):
        sudoku_solver = SudokuSolver(self.puzzle)
        if sudoku_solver.solve_step():
            self.update_canvas()
        else:
            messagebox.showinfo("Fine", "Il Sudoku è già risolto.")

    def update_canvas(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_puzzle()

class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.range_of_possible_num = self.size

    def solve(self):
        empty_position = self.find_empty_position()

        if not empty_position:
            return True

        row, col = empty_position

        for num in range(1, self.range_of_possible_num + 1):
            if self.is_valid(num, row, col):
                self.puzzle[row][col] = num

                if self.solve():
                    return True

                self.puzzle[row][col] = 0

        return False

    def is_valid(self, num, row, col):
        if num in self.puzzle[row]:
            return False

        if num in [self.puzzle[i][col] for i in range(self.size)]:
            return False

        submatrix_size = int(self.size**0.5)
        start_row, start_col = submatrix_size * (row // submatrix_size), submatrix_size * (col // submatrix_size)
        for i in range(start_row, start_row + submatrix_size):
            for j in range(start_col, start_col + submatrix_size):
                if self.puzzle[i][j] == num:
                    return False

        return True

    def find_empty_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 0:
                    return i, j
        return None

    def solve_step(self):
        empty_position = self.find_empty_position()

        if not empty_position:
            return False

        row, col = empty_position

        for num in range(1, self.range_of_possible_num + 1):
            if self.is_valid(num, row, col):
                self.puzzle[row][col] = num
                return True

        return False

if __name__ == "__main__":
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

    selected_problem = 1

    root = tk.Tk()
    sudoku_solver_gui = SudokuSolverGUI(root, problems[selected_problem])
    root.mainloop()
