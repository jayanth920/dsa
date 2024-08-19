# BACKTRACKING
def solve(n):
    cache = {}

    def helper(count, paste):
        if count == n:
            return 0
        if count > n:
            return 1000
        if (count, paste) in cache:
            return cache[(count, paste)]

        # paste
        res1 = 1 + helper(count + paste, paste)

        # copy and paste
        res2 = 2 + helper(count + count, count)

        cache[(count, paste)] = min(res1, res2)
        return cache[(count, paste)]

    if n == 1:
        return 0
    return 1 + helper(1, 1)

# DP SOLUTION - BUT SLOWER, BUT LESS MEMORY
# def solve(n):
#         dp = [1000] * (n + 1)
#         dp[1] = 0
#         for i in range(2, n + 1):
#             for j in range(1, 1 + (i // 2)):
#                 if i % j == 0:
#                     dp[i] = min(dp[i], dp[j] + i // j)

#         return dp[n]