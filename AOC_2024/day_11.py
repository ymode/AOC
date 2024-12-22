def transform_stone(stone):
    if stone == 0:
        return [1]
    s_stone = str(stone)
    if len(s_stone) % 2 == 0:
        mid = len(s_stone) // 2
        left = int(s_stone[:mid])
        right = int(s_stone[mid:])
        return [left, right]
    else:
        return [stone * 2024]

def simulate(initial_stones, num_blinks):
    stones = list(initial_stones)
    for _ in range(num_blinks):
        new_stones = []
        for stone in stones:
            transformed = transform_stone(stone)
            new_stones.extend(transformed)
        stones = new_stones
    return len(stones)

# Read input
with open("day_11.txt", "r") as f:
    line = f.readline().strip()
    initial_stones = [int(x) for x in line.split()]

num_blinks = 25
result = simulate(initial_stones, num_blinks)
print(result)