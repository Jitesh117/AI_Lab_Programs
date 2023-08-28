from heapq import heappop, heappush
from collections import namedtuple

# Define a named tuple to represent puzzle states
PuzzleState = namedtuple("PuzzleState", ["board", "cost", "heuristic", "move", "parent"])

# Define the target state (goal configuration)
target_state = ((1, 2, 3), (8, 0, 4), (7, 6, 5))

# Define possible moves (up, down, left, right)
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
move_names = ["Up", "Down", "Left", "Right"]

# Calculate the Manhattan distance heuristic for a given state
def calculate_manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

# Get possible next states from a given state
def get_next_states(state):
    next_states = []
    empty_row, empty_col = None, None

    # Find the position of the blank space
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_row, empty_col = i, j
                break

    # Generate possible next states by moving tiles into the blank space
    for move, move_name in zip(moves, move_names):
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(row) for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            next_states.append((new_state, move_name))
    
    return next_states

# A* search algorithm
def solve_8_puzzle(initial_state):
    initial_cost = 0
    initial_heuristic = calculate_manhattan_distance(initial_state)
    initial_state = PuzzleState(initial_state, initial_cost, initial_heuristic, "", None)
    
    open_list = [initial_state]
    closed_set = set()
    
    while open_list:
        current_state = heappop(open_list)
        if current_state.board == target_state:
            return current_state
        closed_set.add(tuple(tuple(row) for row in current_state.board))
        
        next_states = get_next_states(current_state.board)
        for next_state, move_name in next_states:
            next_cost = current_state.cost + 1
            next_heuristic = calculate_manhattan_distance(next_state)
            next_state = PuzzleState(next_state, next_cost, next_heuristic, move_name, current_state)
            
            if tuple(tuple(row) for row in next_state.board) not in closed_set:
                heappush(open_list, next_state)
    
    return None

# Print the solution path or indicate unsolvability
def print_solution(solution_state):
    if solution_state is None:
        print("Unsolvable.")
        for i, move in enumerate(moves):
            print(f"Step {i + 1}: {move}")
        return
    moves = []
    while solution_state.parent is not None:
        moves.append(solution_state.move)
        solution_state = solution_state.parent
    moves.reverse()
    print("Solution Path:")
    for i, move in enumerate(moves):
        print(f"Step {i + 1}: {move}")

# Example usage
initial_state = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
solution_state = solve_8_puzzle(initial_state)
print_solution(solution_state)
