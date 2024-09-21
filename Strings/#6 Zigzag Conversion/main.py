from math import ceil

def solve(s, n):
    # Initialize a dictionary to hold rows
    my = {i: "" for i in range(n)}

    if n == 1 or n >= len(s):
        return s  # Handle edge cases

    i = 0  # Pointer for the string
    while i < len(s):
        # Fill top to bottom
        for j in range(n):
            if i < len(s):
                my[j] += s[i]
                i += 1
        
        # Fill bottom to top
        for j in range(n - 2, 0, -1):
            if i < len(s):
                my[j] += s[i]
                i += 1

    # Concatenate all rows to get the final result
    result = ''.join(my[i] for i in range(n))
    return result

# Example usage:
s1 = "PAYPALISHIRING"
numRows1 = 3
print(solve(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

s2 = "PAYPALISHIRING"
numRows2 = 4
print(solve(s2, numRows2))  # Output: "PINALSIGYAHRPI"

