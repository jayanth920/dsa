def solve(s):
    if not s:
        return s

    n = len(s)
    store = n - 1  # To store the point where the palindrome breaks

    for i in range(n):
        j = n - 1  # Start j at the end of the string for each i
        while j >= i:
            if s[i] == s[j]:  # Match found
                # Check if we've reached the middle of the palindrome
                if j == i or j == i + 1:  # Even length
                    store = j
                    break
                j -= 1  # Continue checking backwards
            else:
                store = j  # Mismatch found, store the last matching point
                break

    # Prepend the necessary characters from the reverse of the string
    to_prepend = s[store:][::-1]
    return to_prepend + s

print(solve("aacecaaa"))
# print(solve("abcd"))  # dcbabcd
# print(solve("rjja"))  # ajjrjja
# print(solve("rrjj"))  # jjrrjj
# print(solve("rrja"))  # ajrrja
