def isvalid(state, jug1, jug2, child_nodes):
    if state not in child_nodes:
        if state[0] >= 0 and state[0] <= jug1 and state[1] >= 0 and state[1] <= jug2:
            return True
        else:
            return False
    else:
        return False


def find_possibilities(curr_state, jug1, jug2, possibilites, visited, child_nodes):
    possibilites[curr_state] = set()

    # 6 operations are possible at each stage:

    # 1.Fill Jug1 - (jug1, b)
    new_state = curr_state
    new_state = (jug1, new_state[1])

    if isvalid(new_state, jug1, jug2, child_nodes):
        child_nodes.add(new_state)
        possibilites[curr_state].add(new_state)

    # 2.Fill Jug2 - (a, jug2)
    new_state = curr_state
    new_state = (new_state[0], jug2)

    if isvalid(new_state, jug1, jug2, child_nodes):
        child_nodes.add(new_state)
        possibilites[curr_state].add(new_state)

    # 3.Empty Jug1 (only when a > 0) - (0, b)
    new_state = curr_state
    new_state = (0, new_state[1])

    if isvalid(new_state, jug1, jug2, child_nodes):
        child_nodes.add(new_state)
        possibilites[curr_state].add(new_state)

    # 4.Empty Jug2 (only when b > 0) - (a, 0)
    new_state = curr_state
    new_state = (new_state[0], 0)

    if isvalid(new_state, jug1, jug2, child_nodes):
        child_nodes.add(new_state)
        possibilites[curr_state].add(new_state)

    # 5. Pour water from A to B (only if b < jug2 and a > 0)
    #       empty_space = jug2 - b
    #       if(a >= empty_space):
    #           (a - empty_space, jug2)
    #       else:
    #           (0, b + a)

    new_state = curr_state
    if new_state[1] < jug2 and new_state[0] > 0:
        empty_space = jug2 - new_state[1]
        if new_state[0] >= empty_space:
            new_state = (new_state[0] - empty_space, jug2)
            if isvalid(new_state, jug1, jug2, child_nodes):
                child_nodes.add(new_state)
                possibilites[curr_state].add(new_state)
        else:
            new_state = (0, new_state[0] + new_state[1])
            if isvalid(new_state, jug1, jug2, child_nodes):
                child_nodes.add(new_state)
                possibilites[curr_state].add(new_state)

    # 6. Pour water from B to A (only if a < jug1 and b > 0)
    #       empty_space = jug1 - a
    #       if(b >= empty_space):
    #           (jug1, b - empty_space)
    #       else:
    #           (b + a, 0)

    new_state = curr_state
    if new_state[0] < jug1 and new_state[1] > 0:
        empty_space = jug1 - new_state[0]
        if new_state[1] >= empty_space:
            new_state = (jug1, new_state[1] - empty_space)
            if isvalid(new_state, jug1, jug2, child_nodes):
                child_nodes.add(new_state)
                possibilites[curr_state].add(new_state)
        else:
            new_state = (new_state[0] + new_state[1], 0)
            if isvalid(new_state, jug1, jug2, child_nodes):
                child_nodes.add(new_state)
                possibilites[curr_state].add(new_state)

    return possibilites


def dfs(curr_state, visited, possibilities, jug1, jug2, target, child_nodes):
    print("\ncalling dfs for ", curr_state)

    visited.add(curr_state)
    child_nodes.add(curr_state)

    possibilities = find_possibilities(
        curr_state, jug1, jug2, possibilities, visited, child_nodes
    )
    print(possibilities[curr_state])
    for next in possibilities[curr_state]:
        if next[0] == target or next[1] == target:
            print("Reached target")
            break
        dfs(next, visited, possibilities, jug1, jug2, target, child_nodes)
    return visited


print("\nWATER JUG PROBLEM USING DFS\n")
print("Enter the capacity of ")
jug1 = int(input("Jug 1: "))
jug2 = int(input("Jug 2: "))

target = int(input("Enter the target amount of water: "))

# handling invalid input
while target > jug1 and target > jug2:
    print("The target entered is greater than the capacities of both the jugs!")
    target = int(input("Re-enter the target capacity: "))

# goal state: when the capacity of any jug = target capacity

# To keep the state space tree finite, we can maintain a "visited" list
# If the visited states are not tracked,
#   the state space tree goes infintely and the solution may not be found using DFS

# when all the possibilities from the state are found
visited = set()

possibilities = {}

# to store all the possibilties found - to ensure that we reach target in min num of steps
child_nodes = set()

curr_state = (0, 0)

output = dfs(curr_state, visited, possibilities, jug1, jug2, target, child_nodes)

print(output)
