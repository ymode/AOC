from functools import lru_cache

def split_even(stone_str):
   
    half = len(stone_str) // 2
    left = stone_str[:half]
    right = stone_str[half:]
    # Convert to int to remove leading zeros, then back to str
    left_str = str(int(left))  
    right_str = str(int(right))
    return left_str, right_str

@lru_cache(None)
def count_stones(stone_str, n):
   
    if n == 0:
        return 1

    # If the stone is '0', it becomes '1' immediately
    if stone_str == '0':
        return count_stones('1', n - 1)

    length = len(stone_str)
  
    if length % 2 == 0:
        left_str, right_str = split_even(stone_str)
        return count_stones(left_str, n - 1) + count_stones(right_str, n - 1)
    else:
        # Multiply by 2024
        new_val = int(stone_str) * 2024
        new_str = str(new_val)
        return count_stones(new_str, n - 1)

def solve_part2(filename):
    
    with open(filename, "r") as f:
        line = f.readline().strip()
        initial_stones = [x for x in line.split()]

    total = 0
    for s in initial_stones:
        total += count_stones(s, 75)

    print(total)
    return total

if __name__ == "__main__":
    solve_part2("day_11.txt")
