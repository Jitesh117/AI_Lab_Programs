import random

def suggest_safe_move(board):
    # Given the current state of the Minesweeper board, suggest a safe move.
    safe_moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ' ':
                # Check if revealing this cell is safe based on neighboring mines.
                if is_safe_move(board, row, col):
                    safe_moves.append((row, col))
    if safe_moves:
        return random.choice(safe_moves)
    else:
        return None  # No safe moves available

def is_safe_move(board, row, col):
    # Check if revealing the specified cell is safe based on neighboring mines.
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                if board[nr][nc] == 'M':
                    return False
    return True

# Other Minesweeper game functions and logic...

def main():
    # Initialize the Minesweeper board and other game elements.
    # ...
    
    while not game_over:
        # Player's turn
        player_move = get_player_move()
        if is_valid_move(player_move):
            if is_mine(player_move):
                # Handle mine reveal, end game
                break
            else:
                # Update the board, reveal cells, etc.
                # ...
                
            # AI's turn (Assistive AI)
            ai_suggestion = suggest_safe_move(board)
            if ai_suggestion:
                print("AI suggests:", ai_suggestion)
            
            # Continue the game loop
        
    # Print game outcome (win/loss) and final board

if __name__ == "__main__":
    main()
