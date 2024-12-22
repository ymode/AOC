#!/usr/bin/env python3

def main():
    """
    Part 2 solution:
    - For each integer L in the left list, find how many times L appears in the right list.
    - Add (L * frequency_of_L_in_right_list) to a total similarity score.
    - Print the final total.
    """
    filename = "day1_list.txt"
    
    left_list = []
    right_list = []
    
    # Read the file
    with open(filename, "r") as f:
        lines = f.readlines()
    
    # Parse each line
    for i, line in enumerate(lines, start=1):
        tokens = line.strip().split()
        if len(tokens) != 2:
            # If a line doesn't have exactly two tokens, skip or raise an error
            continue
        left_str, right_str = tokens
        left_num = int(left_str)
        right_num = int(right_str)
        left_list.append(left_num)
        right_list.append(right_num)
    
    # Build a frequency map of all numbers in the RIGHT list
    freq_right = {}
    for val in right_list:
        freq_right[val] = freq_right.get(val, 0) + 1
    
    # Compute the similarity score
    total_similarity = 0
    for L in left_list:
        # If L doesn't appear in freq_right, that means freq_right[L] = 0
        count_in_right = freq_right.get(L, 0)
        total_similarity += L * count_in_right
    
    print(total_similarity)

if __name__ == "__main__":
    main()
