from itertools import permutations
from datetime import datetime, timedelta

class TaskSchedulingCSP:
    def __init__(self, tasks, durations, start_times):
        self.tasks = tasks
        self.durations = durations
        self.start_times = start_times
        self.domains = {task: [(start_time, start_time + timedelta(minutes=d)) for start_time in start_times] for task, d in zip(tasks, durations)}

    def is_valid_assignment(self, assignment):
        for task1, time1 in assignment.items():
            start_time1, end_time1 = time1
            for task2, time2 in assignment.items():
                if task1 != task2:
                    start_time2, end_time2 = time2
                    if start_time2 < end_time1 and end_time2 > start_time1:
                        return False
        return True

    def solve(self):
        for perm in permutations(self.start_times, len(self.tasks)):
            assignment = {task: (start_time, start_time + timedelta(minutes=d)) for task, start_time, d in zip(self.tasks, perm, self.durations)}
            if self.is_valid_assignment(assignment):
                return assignment
        return None

def get_user_input():
    tasks = input("Enter task names separated by commas (e.g., A,B,C): ").split(',')
    durations = [int(x) for x in input("Enter task durations (in minutes) separated by commas: ").split(',')]
    start_times = [datetime.strptime(x, '%H:%M') for x in input("Enter start times for tasks (HH:MM) separated by commas: ").split(',')]
    return tasks, durations, start_times

def print_schedule(schedule):
    for task, (start_time, end_time) in schedule.items():
        print(f"Task {task} scheduled from {start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}")

# Example usage
if __name__ == "__main__":
    tasks, durations, start_times = get_user_input()
    task_scheduling_csp = TaskSchedulingCSP(tasks, durations, start_times)
    solution = task_scheduling_csp.solve()

    if solution:
        print("Solution found:")
        print_schedule(solution)
    else:
        print("No solution found.")
