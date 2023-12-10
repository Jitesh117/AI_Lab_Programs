import random

def initialize_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mine_locations = random.sample(range(rows * cols), num_mines)

    for mine in mine_locations:
        row = mine // cols
        col = mine % cols
        board[row][col] = 'M'

    return board

def print_board(board, revealed):
    print("   " + " ".join([str(i) for i in range(len(board[0]))]))
    for i, row in enumerate(board):
        print(f"{i} |" + "|".join([cell if (i, j) in revealed else " " for j, cell in enumerate(row)]) + "|")

def count_adjacent_mines(board, row, col):
    adjacent_mines = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            r, c = row + dr, col + dc
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'M':
                adjacent_mines += 1
    return adjacent_mines

def uncover_cell(board, revealed, row, col, player):
    if (row, col) in revealed:
        print("You've already uncovered this cell. Choose another one.")
    elif board[row][col] == 'M':
        print(f"Player {player}, you hit a mine! Game over!")
        revealed.update({(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 'M'})
        return False
    else:
        revealed.add((row, col))
        if board[row][col] == ' ':
            adjacent_mines = count_adjacent_mines(board, row, col)
            board[row][col] = str(adjacent_mines)
    return True

def main():
    rows = 5
    cols = 5
    num_mines = 5

    board = initialize_board(rows, cols, num_mines)
    revealed = set()
    player = 1

    print("Welcome to 2-Player Minesweeper!")
    while True:
        print(f"\nPlayer {player}'s turn:")
        print_board(board, revealed)
        try:
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
        except ValueError:
            print("Invalid input. Please enter valid row and column numbers.")
            continue

        if 0 <= row < rows and 0 <= col < cols:
            if uncover_cell(board, revealed, row, col, player):
                if len(revealed) == rows * cols - num_mines:
                    print("Congratulations! The board is clear. It's a draw!")
                    break
                player = 3 - player  # Switch player (1 -> 2, 2 -> 1)
            else:
                break
        else:
            print("Invalid row or column. Please try again.")

if __name__ == "__main__":
    main()
