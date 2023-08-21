# Cost to find the AND and OR path
def Cost(nodes_heuristic, condition, weight, key):
    cost = {}
    if len(condition["AND"]) != 0:
        AND_nodes = condition["AND"]
        # print("AND nodes = ", AND_nodes)
        # x = input()
        Path_A = " AND ".join(i for i in AND_nodes)
        PathA_heuristic = sum(nodes_heuristic[node] + weight for node in AND_nodes)
        # print("and heuristic = ", PathA_heuristic)
        cost[Path_A] = PathA_heuristic
        new_heuristic_values[key] = PathA_heuristic

    if len(condition["OR"]) != 0:
        OR_nodes = condition["OR"]
        # print("OR nodes = ", OR_nodes)
        # x = input()

        Path_B = " OR ".join(i for i in OR_nodes)
        PathB_heuristic = min(nodes_heuristic[node] + weight for node in OR_nodes)
        # print("or heuristic = ", PathB_heuristic)
        cost[Path_B] = PathB_heuristic
        new_heuristic_values[key] = PathB_heuristic

    return cost


# Update the cost
def update_cost(nodes_heuristic, neighbours, weight=1):
    Main_nodes = list(neighbours.keys())
    # print("main nodes = neighbours.keys = ", Main_nodes)
    Main_nodes.reverse()
    least_cost = {}
    for key in Main_nodes:
        condition = neighbours[key]
        # print(
        # key, ":", neighbours[key], ">>>", Cost(nodes_heuristic, condition, weight)
        # )
        c = Cost(nodes_heuristic, condition, weight, key)
        if len(c) > 0:
            nodes_heuristic[key] = min(c.values())
        least_cost[key] = Cost(nodes_heuristic, condition, weight, key)
    return least_cost


# Print the shortest path
def shortest_path(Start, Updated_cost, nodes_heuristic):
    Path = Start
    if Start in Updated_cost.keys():
        try:
            Min_cost = min(Updated_cost[Start].values())
            key = list(Updated_cost[Start].keys())
            values = list(Updated_cost[Start].values())
            Index = values.index(Min_cost)

            # FIND MINIMIMUM PATH KEY
            Next = key[Index].split()
            # ADD TO PATH FOR OR PATH
            if len(Next) == 1:
                Start = Next[0]
                Path += "<--" + shortest_path(Start, Updated_cost, nodes_heuristic)
            # ADD TO PATH FOR AND PATH
            else:
                Path += "<--(" + key[Index] + ") "

                Start = Next[0]
                Path += (
                    "[" + shortest_path(Start, Updated_cost, nodes_heuristic) + " + "
                )

                Start = Next[-1]
                Path += shortest_path(Start, Updated_cost, nodes_heuristic) + "]"
        except ValueError:
            pass
    return Path


#  step 1: Get the graph as input along with the heuristic values
n = int(input("Enter the number of nodes in the directed graph: "))

# neighbours - adjacency list
neighbours = {}

# getting all the nodes along with their heuristic value

nodes_heuristic = {}
initial_heuristic_values = {}
new_heuristic_values = {}

print("Enter the name of each node followed by its heuristic value: ")
for i in range(n):
    name, heuristic = input().split()
    nodes_heuristic[name] = int(heuristic)
    # if nodes_heuristic[name] == -1:
    #     start_node = name
    initial_heuristic_values[name] = int(heuristic)

    neighbours[name] = {}

start_node = input("Enter the start node:")


# getting the neighbours of each of the nodes and the edge weights - they can be stored in the adjacency list neighbours

print("Enter the child nodes of each of these nodes: ")

for i in neighbours:
    print("For ", i, ": ")
    print("AND: ")
    temp_dict = {}
    temp_dict["AND"] = []
    while True:
        userinput = input()
        if userinput:
            inputvalues = userinput.split()
            for x in inputvalues:
                temp_dict["AND"].append(x)
        else:
            break

    print("OR: ")
    temp_dict["OR"] = []
    while True:
        userinput = input()
        if userinput:
            inputvalues = userinput.split()
            for x in inputvalues:
                temp_dict["OR"].append(x)
        else:
            break
    neighbours[i] = temp_dict
"""
nodes_heuristic = {
    "a": -1,
    "b": 5,
    "c": 2,
    "d": 4,
    "e": 7,
    "f": 9,
    "g": 3,
    "h": 0,
    "i": 0,
    "j": 0,
}

new_heuristic_values = {}

neighbours = {
    "a": {"AND": ["c", "d"], "OR": ["b"]},
    "b": {"AND": [], "OR": ["e", "f"]},
    "c": {"AND": ["h", "i"], "OR": ["g"]},
    "d": {"AND": [], "OR": ["j"]},
    "e": {"AND": [], "OR": []},
    "f": {"AND": [], "OR": []},
    "g": {"AND": [], "OR": []},
    "h": {"AND": [], "OR": []},
    "i": {"AND": [], "OR": []},
    "j": {"AND": [], "OR": []},
}
"""

# Updated cost
# print("Neighbours = ", neighbours)
Updated_cost = update_cost(nodes_heuristic, neighbours, weight=1)
# print(new_heuristic_values)
print("Shortest Path :\n", shortest_path(start_node, Updated_cost, nodes_heuristic))
# print("Shortest Path :\n", shortest_path("A", Updated_cost, nodes_heuristic))
print("Node          Actual Cost          Modified cost")
for node in nodes_heuristic:
    try:
        print(
            node,
            "            ",
            initial_heuristic_values[node],
            "                  ",
            min(Updated_cost[node].values()),
        )
    except KeyError:
        print(
            node,
            "            ",
            initial_heuristic_values[node],
            "                  ",
            0,
        )
    except ValueError:
        print(
            node,
            "            ",
            initial_heuristic_values[node],
            "                  ",
            0,
        )


"""
Enter the number of nodes in the directed graph:
10
Enter the name of each node followed by its heuristic value:
a -1
b 5
c 2
d 4
e 7
f 9
g 3
h 0
i 0
j 0
Enter the child nodes of each of these nodes:   
For  a :
AND:
c d

OR:
b

For  b :
AND:

OR:
e
f

For  c :
AND:
h i

OR:
g

For  d :
AND:

OR:
j

For  e :
AND:

OR:

For  f :
AND:

OR:

For  g :
AND:

OR:

For  h :
AND:

OR:

For  i :
AND:

OR:

For  j :
AND:

OR:

"""
