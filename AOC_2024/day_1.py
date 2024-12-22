#!/usr/bin/env python3

def main():
    """
    Reads lines from day1_list.txt. Each line must have exactly two integers
    (e.g. "123 456"). We store the first integer in left_list and the second
    in right_list, then sort each list, and compute the sum of absolute
    differences in sorted order.
    """
    filename = "day1_list.txt"
    
    left_list = []
    right_list = []
    
    # Read the file line by line
    with open(filename, "r") as f:
        lines = f.readlines()
    
    print("[DEBUG] Number of lines found in file:", len(lines))
    
    # Parse each line
    for i, line in enumerate(lines, start=1):
        # Strip leading/trailing whitespace, split on whitespace
        tokens = line.strip().split()
        
        # If the line doesn't have exactly two tokens, log a debug warning
        if len(tokens) != 2:
            print(f"[DEBUG] Warning: line {i} doesn't split into exactly two numbers: {tokens}")
            continue
        
        # Convert tokens to integers
        left_str, right_str = tokens
        left_num = int(left_str)
        right_num = int(right_str)
        
        # Append to lists
        left_list.append(left_num)
        right_list.append(right_num)
    
    # Debug: check lengths
    print("[DEBUG] Number of left items:", len(left_list))
    print("[DEBUG] Number of right items:", len(right_list))
    
    # Sort each list
    left_list.sort()
    right_list.sort()
    
    # Compute sum of absolute differences pairwise
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    
    # Print final result
    print(total_distance)

if __name__ == "__main__":
    main()
