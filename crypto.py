from itertools import permutations

def is_solution_valid(mapping, words, result):
    if any(mapping[word[0]] == 0 for word in words + [result]):
        return False
    
    word_values = [sum(mapping[c] * 10**(len(word)-i-1) for i, c in enumerate(word)) for word in words]
    result_value = sum(mapping[c] * 10**(len(result)-i-1) for i, c in enumerate(result))
    
    return sum(word_values) == result_value

def solve_cryptarithmetic(words, result):
    unique_letters = set(''.join(words + [result]))
    if len(unique_letters) > 10:
        print("Too many unique letters. Cannot solve.")
        return None
    
    letters = list(unique_letters)
    
    for perm in permutations(range(10), len(letters)):
        mapping = {letters[i]: perm[i] for i in range(len(letters))}
        
        if is_solution_valid(mapping, words, result):
            return mapping
    
    return None

def print_solution(mapping, words, result):
    for word in words + [result]:
        print(' '.join(str(mapping[c]) for c in word), end=' ')
        print(f"= {sum(mapping[c] * 10**(len(word)-i-1) for i, c in enumerate(word))}")

def cryptarithmetic_solver(words, result):
    mapping = solve_cryptarithmetic(words, result)
    if mapping is None:
        print("No solution exists.")
    else:
        print_solution(mapping, words, result)

if __name__ == "__main__":
    # Example cryptarithmetic puzzle: SEND + MORE = MONEY
    words = ["SEND", "MORE"]
    result = "MONEY"

    cryptarithmetic_solver(words, result)
