# Sudoku Solver using Backtracking (CSP)

grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def is_valid(row, col, num):
    # Row
    if num in grid[row]:
        return False

    # Column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # 3x3 box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(i, j, num):
                        grid[i][j] = num
                        if solve():
                            return True
                        grid[i][j] = 0
                return False
    return True

solve()

print("Solved Sudoku:")
for row in grid:
    print(row)
