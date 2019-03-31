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

sudoku = [[None for i in range(9)] for j in range(9)]

