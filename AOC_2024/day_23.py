from itertools import combinations

def solve():
    with open("day_23.txt", "r") as f:
        connections = [line.strip() for line in f]

    network = {}
    for connection in connections:
        comp1, comp2 = connection.split('-')
        network.setdefault(comp1, set()).add(comp2)
        network.setdefault(comp2, set()).add(comp1)

    computers = list(network.keys())
    interconnected_sets = set()

    for combo in combinations(computers, 3):
        comp1, comp2, comp3 = combo
        if comp2 in network.get(comp1, set()) and \
           comp3 in network.get(comp1, set()) and \
           comp3 in network.get(comp2, set()):
            interconnected_sets.add(tuple(sorted(combo)))

    count_with_t = 0
    for group in interconnected_sets:
        if any(comp.startswith('t') for comp in group):
            count_with_t += 1

    print(f"Number of interconnected sets of three: {len(interconnected_sets)}")
    print(f"Number of interconnected sets with at least one 't': {count_with_t}")

solve()