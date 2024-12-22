from collections import defaultdict, deque

def solve_part_two():
    with open("day_5.txt") as f:
        raw_content = f.read().strip().split("\n\n")
        raw_rules = raw_content[0].splitlines()
        raw_updates = raw_content[1].splitlines()

    rules = set()
    for rule_str in raw_rules:
        x, y = map(int, rule_str.split("|"))
        rules.add((x, y))

    updates = []
    for update_str in raw_updates:
        updates.append(list(map(int, update_str.split(","))))

    sum_of_middle_pages = 0

    for update in updates:
        is_correct_order = True
        for rule_x, rule_y in rules:
            if rule_x in update and rule_y in update:
                try:
                    index_x = update.index(rule_x)
                    index_y = update.index(rule_y)
                    if index_x > index_y:
                        is_correct_order = False
                        break
                except ValueError:
                    pass

        if not is_correct_order:
            # Reorder the update
            relevant_rules = [(r_x, r_y) for r_x, r_y in rules if r_x in update and r_y in update]

            adj = defaultdict(list)
            in_degree = defaultdict(int)
            nodes = set(update)

            for x, y in relevant_rules:
                adj[x].append(y)
                in_degree[y] += 1

            queue = deque([node for node in nodes if in_degree[node] == 0])
            sorted_update = []

            while queue:
                node = queue.popleft()
                sorted_update.append(node)
                for neighbor in adj[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if len(sorted_update) == len(update):
                middle_index = len(sorted_update) // 2
                sum_of_middle_pages += sorted_update[middle_index]
            else:
                raise Exception("Could not correctly order the update - cycle detected?")

    return sum_of_middle_pages

if __name__ == "__main__":
    result = solve_part_two()
    print(result)