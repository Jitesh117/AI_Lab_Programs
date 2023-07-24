print("\nWATER JUG PROBLEM USING DFS\n")
print("Enter the capacity of ")
jug1 = int(input("Jug 1: "))
jug2 = int(input("Jug 2: "))

target = int(input("Enter the target amount of water: "))

# handling invalid input
while(target > jug1 and target > jug2):
    print("The target entered is greater than the capacities of both the jugs!")
    target = int(input("Re-enter the target capacity: "))

# goal state: when the capacity of any jug = target capacity

# To keep the state space tree finite, we can maintain a "visited" list
# If the visited states are not tracked, 
#   the state space tree goes infintely and the solution may not be found using DFS

visited = []

# 6 operations are possible at each stage:
#1.Fill Jug1 - (jug1, b)        
#2.Fill Jug2 - (a, jug2)
#3.Empty Jug1 (only when a > 0) - (0, b)       
#4.Empty Jug2 (only when b > 0) - (a, 0)
#5. Pour water from A to B (only if b < jug2 and a > 0)
#       empty_space = jug2 - b
#       if(a >= empty_space):
#           (a - empty_space, jug2)
#       else:
#           (0, b + a)

#6. Pour water from B to A (only if a < jug1 and b > 0)
#       empty_space = jug1 - a
#       if(b >= empty_space):
#           (jug1, b - empty_space)
#       else:
#           (b + a, 0)


curr_state = (0, 0)
while(curr_state[0] != target and curr_state[1] != target):
    visited.append(curr_state)
    


