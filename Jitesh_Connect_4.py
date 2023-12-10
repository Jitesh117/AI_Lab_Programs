import numpy as np

# Constants
ROWS = 6
COLS = 7
PLAYER1 = 1
PLAYER2 = 2

def create_board():
    return np.zeros((ROWS, COLS), dtype=int)

def drop_disc(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return True
    return False

def check_winner(board, player):
    # Check rows
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    
    # Check columns
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    
    # Check diagonals
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + i][col + 3 - i] == player for i in range(4)):
                return True
    
    return False

def heuristic_score(board, player):
    score = 0
    opponent = PLAYER2 if player == PLAYER1 else PLAYER1

    # Heuristic values for different lengths of sequences
    scores_dict = {
        1: 1,
        2: 10,
        3: 100,
        4: 1000
    }

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == player:
                # Check horizontally
                for i in range(4):
                    seq = [board[row][col + j] for j in range(i, i + 4)]
                    score += scores_dict.get(seq.count(player), 0)

                # Check vertically
                for i in range(4):
                    seq = [board[row + j][col] for j in range(i, i + 4)]
                    score += scores_dict.get(seq.count(player), 0)

                # Check diagonally (positive slope)
                for i in range(4):
                    seq = [board[row + j][col + j] for j in range(i, i + 4)]
                    score += scores_dict.get(seq.count(player), 0)

                # Check diagonally (negative slope)
                for i in range(4):
                    seq = [board[row + j][col - j] for j in range(i, i + 4)]
                    score += scores_dict.get(seq.count(player), 0)

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == opponent:
                # Check horizontally
                for i in range(4):
                    seq = [board[row][col + j] for j in range(i, i + 4)]
                    score -= scores_dict.get(seq.count(opponent), 0)

                # Check vertically
                for i in range(4):
                    seq = [board[row + j][col] for j in range(i, i + 4)]
                    score -= scores_dict.get(seq.count(opponent), 0)

                # Check diagonally (positive slope)
                for i in range(4):
                    seq = [board[row + j][col + j] for j in range(i, i + 4)]
                    score -= scores_dict.get(seq.count(opponent), 0)

                # Check diagonally (negative slope)
                for i in range(4):
                    seq = [board[row + j][col - j] for j in range(i, i + 4)]
                    score -= scores_dict.get(seq.count(opponent), 0)

    return score

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

def main():
    board = create_board()
    player = PLAYER1

    while True:
        print_board(board)
        col = int(input(f"Player {player}, choose a column (0-{COLS - 1}): "))
        
        if col < 0 or col >= COLS or not drop_disc(board, col, player):
            print("Invalid move! Try again.")
            continue
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if np.count_nonzero(board) == ROWS * COLS:
            print_board(board)
            print("It's a draw!")
            break
        
        player = PLAYER2 if player == PLAYER1 else PLAYER1

if __name__ == "__main__":
    main()
