def solve(n):
    m = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = ""
    for val,symbol in m:
        counter = n // val
        res += (counter * symbol)
        n -= (counter * val)
        
    return res


# Example usage:
print(solve(3749))  # Output: "MMMDCCXLIX"
print(solve(1994))  # Output: "MCMXCIV"
print(solve(58))    # Output: "LVIII"
