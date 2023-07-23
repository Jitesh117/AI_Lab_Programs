# 8 puzzle prblm using bfs

# step 1 - getting the input matrices
init = []
goal = []

print("\n8 PUZZLE PROBLEM USING BFS\n")


#getting initial state as input
print("Enter init state:")
for i in range(3):
    rows = input().split(' ')
    row = []
    for value in rows:
        if(int(value) > 8 or int(value) < 0):
            print("The number must be between ")
        row.append(int(value))
    init.append(row)

#getting the goal state as input
print("Enter goal state:")
for i in range(3):
    rows = input().split(' ')
    row = []
    for value in rows:
        if(int(value) > 8 or int(value) < 0):
            row.append(int(value))
    goal.append(row)


# step 2 - checking if the puzzle is solvable
# It is solvable only if the number of inversions is even
# Invesion - if the order of the 

# creating a dict to the positions of the numbers in the goal state

