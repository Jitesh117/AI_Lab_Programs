#  step 1: Get the graph as input along with the heuristic values
n = int(input("Enter the number of nodes in the directed graph: "))


# dict - adjacency list
dict = {}

# getting all the nodes along with their heuristic value
nodes_heuristic = {}
print("Enter the name of each node followed by its heuristic value: ")
for i in range(n):
    name, heuristic = input().split()
    nodes_heuristic[name] = int(heuristic)

    dict[name] = {}


# getting the neighbours of each of the nodes and the edge weights - they can be stored in the adjacency list dict
print("Enter the neighbours followed by their cost (edge  weights): ")

for j in dict:
    print("For ", j, ": ")
    temp_dict = {}
    while True:
        userinput = input()
        if userinput:
            inputvalues = userinput.split()
            temp_dict[inputvalues[0]] = inputvalues[1]
        else:
            break
    dict[j] = temp_dict

# print(dict)

open_list = []
possible_paths = []

start = input("Enter the start state: ")
goal = input("Enter the goal state: ")

# add start node to open list
open_list.append([start, nodes_heuristic[start]])

while True:
    """
    if the open list is empty,
       print all the paths to the goal
       if possible_paths is empty,
           display that goal state cannot be reached
    """
    if len(open_list) == 0:
        if possible_paths == 0:
            print("The goal node cannot be reached.")
        else:
            print("Possible paths:")
            path_num = 0
            for path in possible_paths:
                path_num += 1
                print("Path ", path_num, ":")
                print(path[0][0], end=" ")
                for i in range(1, len(path[0])):
                    print(" -> ", path[0][i], end="")
                print("    cost = ", path[1])
                print(" ")

            print("SHORTEST PATH: ")
            print(possible_paths[0][0][0], end=" ")
            for i in range(1, len(path[0])):
                try:
                    print(" -> ", possible_paths[0][0][i], end="")
                except(IndexError):
                    pass
            print("")
            print("Cost of the shortest path = ", possible_paths[0][1])
            
        break

    # pick min value of cost from open list
    min = open_list[0][1]
    for path in open_list:
        if path[1] < min:
            min = path[1]

    """
    find all the paths with that min value
    for each of those paths,
        remove the path from open_list
        if the last node in the path is same as goal node,
            add the path to the list of possible_paths
        else
            find the possible paths from that node
            concatenate the neighbour's name to the chosen path
            compute the heuristic value for that path
    """
    print("open list = ", open_list)
    x = input()
    popped_items = []
    indexes = []
    for i in range(0, len(open_list)):
        if open_list[i][1] == min:
            print("popping ", open_list[i], " from open_list")
            temp = open_list[i]
            indexes.append(i)
            popped_items.append(temp)

    indexes.sort(reverse=True)
    for index in indexes:
        open_list.pop(index)

    print("popped items = ", popped_items)
    x = input()
    for item in popped_items:
        if item[0][-1] == goal:
            possible_paths.append(item)
        else:
            # neighbours of item[-1]
            node = item[0][-1]
            print("Neighbours of ", node, ": ", dict[node])
            x = input()
            for neighbour in dict[node]:
                if neighbour not in item[0]:
                    new_path = item[0] + neighbour
                    heuristic = (
                        item[1]
                        - nodes_heuristic[node]
                        + int(dict[node][neighbour])
                        + nodes_heuristic[neighbour]
                    )
                    open_list.append([new_path, heuristic])
