def solve():
    with open("day_22.txt", "r") as f:
        initial_secrets = [int(line.strip()) for line in f]

    def evolve_secret(secret):
        mod = 16777216

        # Step 1
        val = secret * 64
        secret ^= val
        secret %= mod

        # Step 2
        val = secret // 32
        secret ^= val
        secret %= mod

        # Step 3
        val = secret * 2048
        secret ^= val
        secret %= mod

        return secret

    sum_of_2000th_secrets = 0
    for initial_secret in initial_secrets:
        current_secret = initial_secret
        for _ in range(2000):
            current_secret = evolve_secret(current_secret)
        sum_of_2000th_secrets += current_secret

    return sum_of_2000th_secrets

result = solve()
print(result)