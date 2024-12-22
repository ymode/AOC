def solve_part1():
    try:
        with open("day_4.txt", "r") as file:
            grid = [line.strip() for line in file]
    except FileNotFoundError:
        print("Error: day_4.txt not found.")
        return

    rows = len(grid)
    cols = len(grid[0])
    target_word = "XMAS"
    count = 0

    # Directions: horizontal, vertical, diagonal
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if the word fits within the grid boundaries in this direction
                can_form_word = True
                for i in range(len(target_word)):
                    nr, nc = r + dr * i, c + dc * i
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        can_form_word = False
                        break

                if can_form_word:
                    formed_word = "".join(grid[r + dr * i][c + dc * i] for i in range(len(target_word)))
                    if formed_word == target_word:
                        count += 1

    print(f"The word 'XMAS' appears {count} times.")

if __name__ == "__main__":
    solve_part1()