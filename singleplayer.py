import random

# Define the game grid size
GRID_SIZE = 5

# Define player and goal positions
player_position = (0, 0)
goal_position = (GRID_SIZE - 1, GRID_SIZE - 1)

# Define heuristic function (Manhattan distance)
def heuristic(position):
    return abs(position[0] - goal_position[0]) + abs(position[1] - goal_position[1])

# Function to display the game grid
def display_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if (row, col) == player_position:
                print("P", end=" ")
            elif (row, col) == goal_position:
                print("G", end=" ")
            else:
                print(".", end=" ")
        print()

# Main game loop
def main():
    global player_position  # Declare player_position as global
    
    while player_position != goal_position:
        display_grid()
        print("Enter direction: (u)p, (d)own, (l)eft, (r)ight")
        direction = input().lower()
        
        new_position = player_position
        if direction == "u":
            new_position = (max(0, player_position[0] - 1), player_position[1])
        elif direction == "d":
            new_position = (min(GRID_SIZE - 1, player_position[0] + 1), player_position[1])
        elif direction == "l":
            new_position = (player_position[0], max(0, player_position[1] - 1))
        elif direction == "r":
            new_position = (player_position[0], min(GRID_SIZE - 1, player_position[1] + 1))
        
        if heuristic(new_position) < heuristic(player_position):
            player_position = new_position
        else:
            print("Can't move in that direction. Try again.")
    
    display_grid()
    print("Congratulations! You reached the goal!")

if __name__ == "__main__":
    main()
