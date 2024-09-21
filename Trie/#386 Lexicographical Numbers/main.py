def lexicalOrder(n):
    
    res = []
    curr = 1
    for _ in range(n):
        res.append(curr)
        if curr * 10 <= n:
            curr *= 10
        else:
            while (curr // 10) % 10 == 9:
                curr //= 10
            curr += 1
    return res

    # res = []
    # i = 1
    # while i <= n:
    #     res.append(i)
    #     if i * 10 <= n:  # Go deeper
    #         i *= 10
    #     else:
    #         if i >= n:  # If we're at the maximum
    #             i //= 10  # Backtrack one level
    #         i += 1  # Increment to the next number
    #         # Handle trailing zeros while backtracking
    #         while i % 10 == 0:
    #             i //= 10
    #         # If we backtrack and i is still <= n, continue; otherwise, break
    #         if i == n:
    #             break
    # return res

# Test cases
print(lexicalOrder(13))  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
print(lexicalOrder(2))   # Output: [1, 2]
