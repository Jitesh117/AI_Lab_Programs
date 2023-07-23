
#function to get input for init and goal states

def get_state():
    input_state = []
    for i in range(3):
        nums = input().split()
        for num in nums:
            num = int(num)
            if(num > 8 or num < 0):
                print("The numbers must be between 0 and 8")
            elif(num in input_state):
                print(num, " can appear on only one tile")
                print("\nRe-enter the numbers from the beginning")
                input_state = get_state()
            input_state.append(num)
    
    return input_state


def move_top(curr_state):
    state = curr_state[:]
    # swap 0 with the num at (x - 3)rd index
    x = state.index(0)
    state[x] = state[x - 3]
    state[x - 3] = 0 

    return state



def move_right(curr_state):
    state = curr_state[:]
    # swap 0 with the num at (x + 1)rd index
    x = state.index(0)
    state[x] = state[x + 1]
    state[x + 1] = 0 

    return state


def move_bottom(curr_state):
    state = curr_state[:]
    # swap 0 with the num at (x + 3)rd index
    x = state.index(0)
    state[x] = curr_state[x + 3]
    state[x + 3] = 0 

    return state


def move_left(curr_state):
    state = curr_state[:]
    # swap 0 with the num at (x + 1)rd index
    x = state.index(0)
    state[x] = state[x - 1]
    state[x - 1] = 0 

    return state


def print_puzzle(modified_state):
    i = 0

    for i in range(9):
        if(i not in [2, 5, 8]):
            print(modified_state[i], end=" ")
        else:
            print(modified_state[i])



#step 1 - get input for init and goal states
print("\n8 - PUZZLE PROBLEM USING BFS\n")

print("Enter the Initial State: ")
init = get_state()

print("Enter the Goal State: ")
goal = get_state()

if(init == goal):
    print("Initial state is same as the goal state!")
else:

    #step 2 - check if it is solvable
        # if num of inversions is even, solvable
        # if odd, unsolvable

    inversions = 0
    prevGoalPosn = -1

    for tile in init:
        if(tile != 0):
            currGoalPosn = goal.index(tile)
            if(prevGoalPosn > currGoalPosn):
                diff = prevGoalPosn - currGoalPosn
                inversions += diff
            prevGoalPosn = currGoalPosn

    if(inversions % 2 != 0):
        print("\nThis is unsolvable!")
    else:
        print("\nIt is solvable!")
        # list to store the visited states - (acts as a queue - FIFO)
        visited = []
        visited.append(init)

        while(len(visited) > 0):
            curr_state = visited.pop(0)
            print("Finding the possibilities from the state: ")
            print_puzzle(curr_state)


            if(curr_state.index(0) not in [0, 1, 2]):
                print("\nMoving top, ")
                modified_state = move_top(curr_state)
                print_puzzle(modified_state)
                if(modified_state == goal):
                    print("Goal state reached!")
                    break
                visited.append(modified_state)


            if(curr_state.index(0) not in [2, 5, 8]):
                print("\nMoving right, ")
                modified_state = move_right(curr_state)
                print_puzzle(modified_state)
                if(modified_state == goal):
                    print("Goal state reached!")
                    break
                visited.append(modified_state)

            if(curr_state.index(0) not in [6, 7, 8]):
                print("\nMoving bottom, ")
                modified_state = move_bottom(curr_state)
                print_puzzle(modified_state)
                if(modified_state == goal):
                    print("Goal state reached!")
                    break
                visited.append(modified_state)

            if(curr_state.index(0) not in [0, 3, 6]):
                print("\nMoving left, ")
                modified_state = move_left(curr_state)
                print_puzzle(modified_state)
                if(modified_state == goal):
                    print("Goal state reached!")
                    break
                visited.append(modified_state)


