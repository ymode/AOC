def solve():
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
                    # Should not happen if rule_x and rule_y are in update
                    pass
        if not is_correct_order:
            continue

        if is_correct_order:
            middle_index = len(update) // 2
            sum_of_middle_pages += update[middle_index]

    return sum_of_middle_pages

if __name__ == "__main__":
    result = solve()
    print(result)