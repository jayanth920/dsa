def solve(i, j, s, dp):
    if i == j:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    minTurns = float("inf")
    for k in range(i, j):
        minTurns = min(minTurns, solve(i, k, s, dp) + solve(k + 1, j, s, dp))

    dp[i][j] = minTurns if s[i] != s[j] else minTurns - 1
    return dp[i][j]


def strangePrinter(s):
    n = len(s)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return solve(0, n - 1, s, dp)


print(strangePrinter("aaabbb"))
print(strangePrinter("aba"))