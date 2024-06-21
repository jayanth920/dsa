#O(n)
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    left = 0
    maxLength = 0

    for right in range(len(s)):
        # If the character at right pointer is in the set, remove the left-most character and move left pointer
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        # Add the current character to the set
        charSet.add(s[right])
        # Update the maxLength if the current window size is larger
        maxLength = max(maxLength, right - left + 1)

    return maxLength

# Test cases
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
print(lengthOfLongestSubstring(""))          # Output: 0
print(lengthOfLongestSubstring(" "))         # Output: 1
