def solve(s):
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        res = ''.join(filtered_chars)

        return res == res[::-1]
    
print(solve("race a car"))
print(solve("A man, a plan, a canal: Panama"))
print(solve("malayalam"))