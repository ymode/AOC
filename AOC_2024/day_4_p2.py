def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            # Must be an 'A' for the center
            if grid[r][c] != 'A':
                continue
            
            # Check boundaries for the corners of the X
            if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
                continue
            
            top_left     = grid[r - 1][c - 1]
            bottom_right = grid[r + 1][c + 1]
            top_right    = grid[r - 1][c + 1]
            bottom_left  = grid[r + 1][c - 1]
            
          
            if (top_left == 'M' and bottom_right == 'S' and 
                top_right == 'M' and bottom_left == 'S'):
                count += 1
            
            # 2) (M,S) & (S,M)
            if (top_left == 'M' and bottom_right == 'S' and 
                top_right == 'S' and bottom_left == 'M'):
                count += 1
            
            # 3) (S,M) & (M,S)
            if (top_left == 'S' and bottom_right == 'M' and 
                top_right == 'M' and bottom_left == 'S'):
                count += 1
            
            # 4) (S,M) & (S,M)
            if (top_left == 'S' and bottom_right == 'M' and 
                top_right == 'S' and bottom_left == 'M'):
                count += 1
    
    return count


def main():

    with open('day_4.txt', 'r') as f:
        raw_lines = [line.rstrip('\n') for line in f]
    
    # Convert each line into a list of characters, forming a 2D list (grid)
    grid = [list(row) for row in raw_lines]
    
    total_xmas = count_xmas(grid)
    print(f"Number of X-MAS occurrences: {total_xmas}")


if __name__ == "__main__":
    main()
