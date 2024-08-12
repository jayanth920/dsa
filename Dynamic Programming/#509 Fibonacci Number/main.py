def fib(n: int) -> int:
    # METHOD 1 -> More memory, More speed

    if n < 1:
        return 0
    if n == 1:
        return 1
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[len(dp) - 1] + dp[len(dp) - 2]

    # METHOD 2 (recursion) -> Low Memory, Low Speed

    # if n in [0,1]:
    #     return n

    # return self.fib(n-1) + self.fib(n-2)
