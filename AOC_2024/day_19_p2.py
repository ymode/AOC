#!/usr/bin/env python3

def count_ways(design, patterns_set):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1 

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] != 0 and design[j:i] in patterns_set:
                dp[i] += dp[j]

    return dp[n]

def main():
    with open('day_19.txt', 'r') as f:
       
        patterns_line = f.readline().strip()
        
        blank_line = f.readline()  
        
        designs = [line.strip() for line in f if line.strip()]

    patterns = [p.strip() for p in patterns_line.split(',')]

    patterns_set = set(patterns)
    
    total_ways = 0
    for design in designs:
        total_ways += count_ways(design, patterns_set)
    
    print(total_ways)

if __name__ == "__main__":
    main()
