def solve_part2_efficient():
    with open("day_22.txt", "r") as f:
        initial_secrets = [int(line.strip()) for line in f]
    
    MOD = 16777216
    
    def evolve_secret(secret):
        # Step 1
        val = secret * 64
        secret ^= val
        secret %= MOD

        # Step 2
        val = secret // 32
        secret ^= val
        secret %= MOD

        # Step 3
        val = secret * 2048
        secret ^= val
        secret %= MOD

        return secret

   
    aggregator = {}
    
    for initial_secret in initial_secrets:
        # Generate 2000 new secrets
        secrets = [initial_secret]
        cur = initial_secret
        for _ in range(2000):
            cur = evolve_secret(cur)
            secrets.append(cur)
        
        prices = [s % 10 for s in secrets]  # length 2001
       
        changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]  # length 2000
        
      
        buyer_dict = {}
        
        for i in range(len(changes) - 3):
            pattern = (changes[i], changes[i+1], changes[i+2], changes[i+3])
            if pattern not in buyer_dict:
                buyer_dict[pattern] = prices[i+4]
        
       
        for pattern, sale_price in buyer_dict.items():
            aggregator[pattern] = aggregator.get(pattern, 0) + sale_price
    
   
    best_sum = 0
    best_pattern = None
    for pattern, total_sale_price in aggregator.items():
        if total_sale_price > best_sum:
            best_sum = total_sale_price
            best_pattern = pattern
    
    print("Best 4-change pattern:", best_pattern)
    print("Max total bananas:", best_sum)

if __name__ == "__main__":
    solve_part2_efficient()
