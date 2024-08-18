def solve(points):
        m, n = len(points), len(points[0])
        dp = points[0]

        for r in range(1, m):
            # Left-to-Right pass
            left = [0] * n
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c - 1] - 1, dp[c])

            # Right-to-Left pass
            right = [0] * n
            right[-1] = dp[-1]
            for c in range(n - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, dp[c])

            # Update dp for the current row
            for c in range(n):
                dp[c] = points[r][c] + max(left[c], right[c])

        return max(dp)
       
print(solve([[1,2,3],[1,5,1],[3,1,1]]))
print(solve([[1,5],[2,3],[4,2]]))

# print(maxxer([1,2,3,4,88,67]))
            
    