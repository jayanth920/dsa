def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    str_x = str(x)
    
    return str_x == str_x[::-1]

# Test cases
print(isPalindrome(121))  # Output: True
print(isPalindrome(-121)) # Output: False
print(isPalindrome(10))   # Output: False