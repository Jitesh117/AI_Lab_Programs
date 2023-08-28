def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def is_valid_position(board, word, row, col, direction):
    rows, cols = len(board), len(board[0])

    if direction == "horizontal":
        return col + len(word) <= cols and all(board[row][col + i] == word[i] or board[row][col + i] == "." for i in range(len(word)))
    elif direction == "vertical":
        return row + len(word) <= rows and all(board[row + i][col] == word[i] or board[row + i][col] == "." for i in range(len(word)))
    elif direction == "diagonal":
        return row + len(word) <= rows and col + len(word) <= cols and all(board[row + i][col + i] == word[i] or board[row + i][col + i] == "." for i in range(len(word)))
    else:
        return False

def solve_word_search(board, words):
    rows, cols = len(board), len(board[0])

    for word in words:
        for row in range(rows):
            for col in range(cols):
                for direction in ["horizontal", "vertical", "diagonal"]:
                    if is_valid_position(board, word, row, col, direction):
                        if direction == "horizontal":
                            for i in range(len(word)):
                                board[row][col + i] = word[i]
                        elif direction == "vertical":
                            for i in range(len(word)):
                                board[row + i][col] = word[i]
                        elif direction == "diagonal":
                            for i in range(len(word)):
                                board[row + i][col + i] = word[i]
                        break

def word_search_solver(board, words):
    solve_word_search(board, words)
    print_grid(board)

if __name__ == "__main__":
    # Example word search grid and words
    grid = [
        ["E", "A", "R", "T"],
        ["N", "I", "N", "E"],
        ["E", "N", "D", "E"],
        ["A", "N", "D", "Y"]
    ]
    word_list = ["EAT", "AND", "ART", "DEN", "END", "TINE", "DEAR"]

    word_search_solver(grid, word_list)
