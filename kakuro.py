def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

def is_valid(grid, row, col, value):
    # Check the column
    if any(grid[i][col] == value for i in range(9)):
        return False
    
    # Check the row
    if value in grid[row]:
        return False
    
    return True

def solve_kakuro(grid, clues):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for value in range(1, 10):
                    if is_valid(grid, row, col, value):
                        grid[row][col] = value
                        if solve_kakuro(grid, clues):
                            return True
                        grid[row][col] = 0  # Backtrack
                return False  # No valid value found
    return True

def kakuro_solver(grid, clues):
    if solve_kakuro(grid, clues):
        print("Kakuro solved:")
        print_grid(grid)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    # Example Kakuro grid and clues
    kakuro_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    kakuro_clues = [
        [(0, 0), (0, 1), 3],
        [(1, 0), (1, 1), 4],
        [(2, 0), (2, 1), 17],
        [(0, 0), (1, 0), 10],
        [(0, 2), (0, 3), 7],
        [(0, 1), (1, 1), 3],
        [(1, 2), (1, 3), 9],
        [(2, 2), (2, 3), 4],
        [(0, 2), (1, 2), 16]
    ]

    for clue in kakuro_clues:
        start, end, value = clue
        start_row, start_col = start
        end_row, end_col = end
        for row in range(start_row, end_row + 1):
            for col in range(start_col, end_col + 1):
                kakuro_grid[row][col] = -1  # Mark clue cells with -1

    kakuro_solver(kakuro_grid, kakuro_clues)
