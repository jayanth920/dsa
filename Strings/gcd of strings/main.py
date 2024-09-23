def solve(str1,str2):
        res = []
        # Helper function to check if one string divides the other
        def divides(s, t):
            return s == t * (len(s) // len(t))
        
        # Find the greatest common divisor of the lengths of str1 and str2
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Find the greatest common divisor of the lengths of the strings
        gcd_length = gcd(len(str1), len(str2))
        
        # Candidate for the gcd string is the prefix of str1 up to gcd_length
        candidate = str1[:gcd_length]
        
        # Check if this candidate divides both strings
        if divides(str1, candidate) and divides(str2, candidate):
            return candidate
        else:
            return ""
                
            
            
print(solve("ABCABC", "ABC")) #ABC
print(solve("ABABAB", "ABAB")) #AB
print(solve("LEET", "CODE"))