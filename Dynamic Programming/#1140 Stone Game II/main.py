def solve(piles):
    # EXCELLENT
    dp = {}  # Memoization dictionary

    def dfs(alice, i, M):
        if i == len(piles):
            return 0
        if (alice, i, M) in dp:
            return dp[(alice, i, M)]

        res = 0 if alice else float("inf")
        total = 0

        for X in range(1, 2 * M + 1):
            if i + X > len(piles):
                break
            total += piles[i + X - 1]

            if alice:
                res = max(res, total + dfs(not alice, i + X, max(M, X)))
            else:
                res = min(res, dfs(not alice, i + X, max(M, X)))

        dp[(alice, i, M)] = res
        return res

    return dfs(True, 0, 1)

    # EXCELLENT
    # @lru_cache(None)
    # def play(i, m):
    #     s = sum(piles[i:])
    #     if i + 2 * m >= len(piles):
    #         return s
    #     return s - min(play(i + x, max(m, x)) for x in range(1, 2 * m + 1))
    # return play(0, 1)

    # Test Cases


# Test Case 1: Basic Test
piles = [2, 7, 9, 4, 4]
print(solve(piles))  # Expected output: 10

# Test Case 2: All piles have equal stones
piles = [4, 4, 4, 4, 4, 4]
print(solve(piles))  # Expected output: 12

# Test Case 3: Increasing order of stones
piles = [1, 2, 3, 4, 5, 6]
print(solve(piles))  # Expected output: 12

# Test Case 4: Large number of piles
piles = [1] * 100
print(solve(piles))  # Expected output: 50

# Test Case 5: Single pile
piles = [5]
print(solve(piles))  # Expected output: 5

# Test Case 6: Alice can take all
piles = [100, 200, 300, 400]
print(solve(piles))  # Expected output: 500
