def is_safe(board, row, col, N):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row, N):
    if row >= N:
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, N):
                return True
            board[row][col] = 0
    
    return False

def print_solution(board):
    for row in board:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))

def nqueens_solver(N):
    board = [[0] * N for _ in range(N)]
    
    if not solve_nqueens(board, 0, N):
        print("No solution exists.")
    else:
        print_solution(board)

if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard (N): "))
    nqueens_solver(N)
