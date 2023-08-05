# to represent each node in the graph
# name is the name of the node
# heuristic is the estimated distance from the node to the goal state
# the node with heuristic value = 0 is the goal state
# (since, distance to reach the goal state is 0)

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic


#  step 1: Get the graph as input along with the heuristic values
n = int(input("Enter the number of nodes in the directed graph: "))


# dict - adjacency list
dict = {}

# getting all the nodes along with their heuristic value
print("Enter the name of each node followed by its heuristic value: ")
for i in range(n):
    name, heuristic = input().split()
    graph_node = Node(name, heuristic)

    dict[graph_node] = {}
    

# getting the neighbours of each of the nodes and the edge weights - they can be stored in the adjacency list dict
print("Enter the neighbours followed by their cost (edge  weights): ")

for j in dict:
    print("For ", j.name, ": ")
    temp_dict = {}
    while True:
        node_name, weight = input().split()
        if not node_name:
            break
        temp_dict[node_name] = weight
    j = temp_dict

print(dict)


