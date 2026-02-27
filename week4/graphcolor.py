import matplotlib.pyplot as plt

# -----------------------------
# CSP BACKTRACKING SOLVER
# -----------------------------

def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True


def backtrack(assignment, graph, colors):
    if len(assignment) == len(graph):
        return assignment

    unassigned = [r for r in graph if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color
            result = backtrack(assignment, graph, colors)
            if result:
                return result
            del assignment[region]

    return None


# -----------------------------
# VISUALIZATION FUNCTION
# -----------------------------

def plot_map(solution):
    # Approximate positions of regions
    positions = {
        "WA": (1, 3),
        "NT": (3, 4),
        "SA": (3, 2),
        "Q": (5, 4),
        "NSW": (5, 2),
        "V": (5, 1),
        "T": (5, 0)
    }

    plt.figure(figsize=(8, 6))

    for region, (x, y) in positions.items():
        plt.scatter(x, y, s=4000, color=solution[region], edgecolors='black')
        plt.text(x, y, region, ha='center', va='center', fontsize=12, color='white')

    # Draw connections (edges)
    edges = [
        ("WA", "NT"), ("WA", "SA"),
        ("NT", "SA"), ("NT", "Q"),
        ("SA", "Q"), ("SA", "NSW"), ("SA", "V"),
        ("Q", "NSW"),
        ("NSW", "V")
    ]

    for r1, r2 in edges:
        x_values = [positions[r1][0], positions[r2][0]]
        y_values = [positions[r1][1], positions[r2][1]]
        plt.plot(x_values, y_values, 'k-')

    plt.title("Map Coloring Solution (CSP with Backtracking)")
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.show()


# -----------------------------
# MAIN
# -----------------------------

def main():
    graph = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["SA", "Q", "V"],
        "V": ["SA", "NSW"],
        "T": []
    }

    colors = ["red", "green", "blue"]

    solution = backtrack({}, graph, colors)

    if solution:
        print("Solution Found:\n")
        for region in solution:
            print(region, "->", solution[region])
        plot_map(solution)
    else:
        print("No solution exists.")


if __name__ == "__main__":
    main()