from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    def is_valid_state(j1, j2):
        return 0 <= j1 <= jug1_capacity and 0 <= j2 <= jug2_capacity

    def get_next_states(j1, j2):
        # All possible actions: fill jug 1, fill jug 2, empty jug 1, empty jug 2,
        # pour from jug 1 to jug 2, pour from jug 2 to jug 1.
        actions = [(jug1_capacity, j2),
                   (j1, jug2_capacity),
                   (0, j2),
                   (j1, 0),
                   (min(j1 + j2, jug1_capacity), max(0, j1 + j2 - jug1_capacity)),
                   (max(0, j1 + j2 - jug2_capacity), min(j1 + j2, jug2_capacity))]
        return [(x, y) for x, y in actions if is_valid_state(x, y)]

    def find_path():
        visited = set()
        queue = deque([(0, 0, [])])

        while queue:
            j1, j2, path = queue.popleft()

            if (j1, j2) in visited:
                continue

            visited.add((j1, j2))

            if j1 == target_amount or j2 == target_amount:
                return path + [(j1, j2)]

            next_states = get_next_states(j1, j2)

            for next_j1, next_j2 in next_states:
                queue.append((next_j1, next_j2, path + [(j1, j2)]))

        return None

    return find_path()


if __name__ == "__main__":
    jug1_capacity = int(input("Enter the capacity of the first jug: "))
    jug2_capacity = int(input("Enter the capacity of the second jug: "))
    target_amount = int(input("Enter the target amount of water: "))

    solution = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

    if solution:
        print("Steps to achieve the target amount:")
        for i, (j1, j2) in enumerate(solution):
            print(f"Step {i + 1}: Jug 1: {j1} units, Jug 2: {j2} units")
    else:
        print("Target amount cannot be achieved with the given jug capacities.")
