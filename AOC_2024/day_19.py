def can_form_design(design, patterns_set):
    """
    Returns True if 'design' can be formed by concatenating
    any number of patterns in 'patterns_set', else False.
    """
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True  
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and design[j:i] in patterns_set:
                dp[i] = True
                break
    return dp[n]

def main():
    with open('day_19.txt', 'r') as f:
        patterns_line = f.readline().strip()
        
        blank_line = f.readline()  
        
        designs = [line.strip() for line in f if line.strip()]
    
    patterns = [p.strip() for p in patterns_line.split(',')]
    
    # Convert the list of patterns to a set for O(1) lookup
    patterns_set = set(patterns)
    
    possible_count = 0
    for design in designs:
        if can_form_design(design, patterns_set):
            possible_count += 1
    
    print(possible_count)

if __name__ == "__main__":
    main()
