def solve(piles):
    dp = {}  # Subarray Piles (L,R)

    def dfs(L, R):  # For Alice Only
        if L > R:
            return 0
        if (L, R) in dp:
            return dp[(L, R)]

        even = True if (R - 1) % 2 else False

        left = piles[L] if even else 0
        right = piles[R] if even else 0

        dp[(L, R)] = max(dfs(L + 1, R) + left, dfs(L, R - 1) + right)

        return dp[(L, R)]

    return dfs(0, len(piles) - 1) > (sum(piles)) // 2


print(solve([5, 3, 4, 5]))
print(solve([3, 7, 2, 3]))
