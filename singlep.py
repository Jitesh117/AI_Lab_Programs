import tkinter as tk
from tkinter import messagebox
import random

# Define the game grid size
GRID_SIZE = 5

# Define player and goal positions
player_position = (0, 0)
goal_position = (GRID_SIZE - 1, GRID_SIZE - 1)

# Define the number of obstacles and generate random obstacle positions
NUM_OBSTACLES = 5
obstacle_positions = [(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)) for _ in range(NUM_OBSTACLES)]

# Define heuristic function (Manhattan distance)
def heuristic(position):
    return abs(position[0] - goal_position[0]) + abs(position[1] - goal_position[1])

# Function to update the game grid
def update_grid():
    canvas.delete("all")
    cell_size = 50
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x1, y1 = col * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            if (row, col) == player_position:
                canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            elif (row, col) == goal_position:
                canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            elif (row, col) in obstacle_positions:
                canvas.create_rectangle(x1, y1, x2, y2, fill="red")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    
# Function to handle player movement
def move(direction):
    global player_position
    
    new_position = player_position
    if direction == "u":
        new_position = (max(0, player_position[0] - 1), player_position[1])
    elif direction == "d":
        new_position = (min(GRID_SIZE - 1, player_position[0] + 1), player_position[1])
    elif direction == "l":
        new_position = (player_position[0], max(0, player_position[1] - 1))
    elif direction == "r":
        new_position = (player_position[0], min(GRID_SIZE - 1, player_position[1] + 1))
    
    if new_position not in obstacle_positions and heuristic(new_position) < heuristic(player_position):
        player_position = new_position
        update_grid()
        if player_position == goal_position:
            messagebox.showinfo("Congratulations", "You reached the goal!")

# Create the main window
root = tk.Tk()
root.title("Heuristic Game with Random Obstacles")

# Create a canvas for the game grid
canvas = tk.Canvas(root, width=GRID_SIZE * 50, height=GRID_SIZE * 50)
canvas.pack()

# Create buttons for player movement
up_button = tk.Button(root, text="Up", command=lambda: move("u"))
up_button.pack(side="left")
down_button = tk.Button(root, text="Down", command=lambda: move("d"))
down_button.pack(side="left")
left_button = tk.Button(root, text="Left", command=lambda: move("l"))
left_button.pack(side="left")
right_button = tk.Button(root, text="Right", command=lambda: move("r"))
right_button.pack(side="left")

# Initialize the game grid
update_grid()

# Start the Tkinter main loop
root.mainloop()
