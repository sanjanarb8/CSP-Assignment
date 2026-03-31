# Australia Map Coloring using CSP (Backtracking)

states = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

# Adjacency list (constraints)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

# Check if assignment is valid
def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment

    for state in states:
        if state not in assignment:
            for color in colors:
                if is_valid(state, color, assignment):
                    assignment[state] = color
                    result = backtrack(assignment)
                    if result:
                        return result
                    del assignment[state]
            return None

solution = backtrack({})
print("Australia Map Coloring Solution:")
print(solution)
