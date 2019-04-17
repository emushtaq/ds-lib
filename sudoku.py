import numpy as np
import time
"""
A Sudoku solver
"""

#  - Create a DS for holding the puzzle
#  - Write a validator that validates each input
#  - Write a Sanity Checker for entire puzle ??
#  - Implement a backtracking solution to solve the puzzle


"""
Sample Input:
* * 7 | * 8 * | * 3 *
* * * | * * * | 2 6 9
* 6 * | * 1 9 | * * 7
---------------------
* 9 2 | * 4 * | * * *
8 * * | 3 * 5 | * * 4
* * * | * 9 * | 3 1 *
---------------------
6 * * | 7 5 * | * 8 *
* 8 9 | * * * | * * *
* 3 * | * 6 * | 5 * *
"""


"""
Sample Output:
9 4 7 | 6 8 2 | 1 3 5
1 5 8 | 4 7 3 | 2 6 9
2 6 3 | 5 1 9 | 8 4 7
---------------------
3 9 2 | 1 4 7 | 6 5 8
8 1 6 | 3 2 5 | 7 9 4
4 7 5 | 8 9 6 | 3 1 2
---------------------
6 2 1 | 7 5 4 | 9 8 3
5 8 9 | 2 3 1 | 4 7 6
7 3 4 | 9 6 8 | 5 2 1
"""

solution = [[9, 4, 7, 6, 8, 2, 1, 3, 5],
            [1, 5, 8, 4, 7, 3, 2, 6, 9],
            [2, 6, 3, 5, 1, 9, 8, 4, 7],
            [3, 9, 2, 1, 4, 7, 6, 5, 8],
            [8, 1, 6, 3, 2, 5, 7, 9, 4],
            [4, 7, 5, 8, 9, 6, 3, 1, 2],
            [6, 2, 1, 7, 5, 4, 9, 8, 3],
            [5, 8, 9, 2, 3, 1, 4, 7, 6],
            [7, 3, 4, 9, 6, 8, 5, 2, 1]]


EMPTY = 0


def getInput():
    input = input()
    if input == "*":
        return None
    return input


def convert_input(value):
    if value == "*":
        return EMPTY
    else:
        return int(value)


def is_valid_set(values):
    return len(set(values)) == len(values)


def are_rows_valid(sudoku):
    for row in sudoku:
        if (EMPTY in row) or not is_valid_set(row):
            print(f"Row {row} is invalid.")
            return False
    return True


def is_value_in_row(sudoku, value, row):
    pass


def is_value_in_col(sudoku, value, col):
    pass


def is_value_in_cell(sudoku, value, cell):
    pass


def are_cols_valid(sudoku):
    for col in np.transpose(sudoku):
        if (EMPTY in col) or not is_valid_set(col):
            print(f"Col {col} is invalid.")
            return False
    return True


def are_cells_valid(sudoku):
    cells = []
    offset = 3
    for i in range(0, len(sudoku), 3):  # row cell offset
        for j in range(0, len(sudoku), 3):  # col cell offset
            cells.append(sudoku[i: i + offset, j: j + offset].reshape(-1))

    for cell in cells:
        if (EMPTY in cell) or not is_valid_set(cell):
            print(f"Cell {cell} is invalid.")
            return False

    return True


def is_safe(sudoku):
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] == EMPTY:
                return False


def solve(sudoku):
    for line in sudoku:
        for value in line:
            if value == 0:
                for i in range(1, 10):
                    value = i

                    if value not in line:  # check for value in row
                        if value not in 

if __name__ == "__main__":
    print("-----------  SUDOKU SOLVER -----------")
    # print(" Enter the inputs for the puzzle. \
    # Enter '*' when there are no inputs")
    # TODO sudoku = [[input() for i in range(9)] for j in range(9)]

    sudoku = [
        ["*", "*", "7", "*", "8", "*", "*", "3", "*"],
        ["*", "*", "*", "*", "*", "*", "2", "6", "9"],
        ["*", "6", "*", "*", "1", "9", "*", "*", "7"],
        ["*", "9", "2", "*", "4", "*", "*", "*", "*"],
        ["8", "*", "*", "3", "*", "5", "*", "*", "4"],
        ["*", "*", "*", "*", "9", "*", "3", "1", "*"],
        ["6", "*", "*", "7", "5", "*", "*", "8", "*"],
        ["*", "8", "9", "*", "*", "*", "*", "*", "*"],
        ["*", "3", "*", "*", "6", "*", "5", "*", "*"]
    ]

    start = time.time()
    print("Solving the puzzle : ")
    sudoku = [[convert_input(value) for value in line] for line in sudoku]

    sudoku, solution = np.array(sudoku), np.array(solution)


    # print("Validity : ", are_rows_valid(sudoku))
    # print("Validity : ", are_cols_valid(sudoku))
    # print("Validity : ", are_cells_valid(sudoku))

    answer = solve(sudoku)
    print(answer)
    end = time.time()

    print(f"The script took {end - start} seconds.")

    pass
