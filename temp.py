# def solve(nums):
#     reachmaxxing = 0
#     for i in range(len(nums)):
#         if i <= reachmaxxing:
#             reachmaxxing = max(reachmaxxing, i+nums[i])
#             if reachmaxxing >= len(nums)-1:
#                 return True
#     return False
    

# def solve(nums):
#     reachmaxxing = len(nums)-1
#     for i in range(len(nums)-2,-1,-1):
#         if i+nums[i] >= reachmaxxing:
#             reachmaxxing = min(reachmaxxing, i-nums[i])
#             if reachmaxxing <= 0:
#                 return True
#     return False

# print(solve([2,3,1,1,4]))

# def findPlatform(arrival, departure):
#     n = len(arrival)
    
#     # Initialize the first departure as max_time
#     max_time = departure[0]
#     c = 1  # Platform counter

#     # Sort both arrays to ensure proper order of events
#     arrival.sort()
#     departure.sort()

#     # Iterate over the arrival array
#     for i in range(n - 1):
#         # If the next train arrives before the current train departs, we need another platform
#         if departure[i] > arrival[i + 1]:
#             c += 1
#         else:
#             # Update max_time if the next train arrives after the current max_time
#             if arrival[i + 1] > max_time:
#                 max_time = departure[i + 1]
#                 c -= 1
    
#     return c

# # Test case
# print(findPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))  # Output: 3
# print(findPlatform([900, 1100, 1235], [1000, 1200, 1240]))  # Output: 1
# print(findPlatform([200, 210, 300, 320, 350, 500], [230, 340, 320, 430, 400, 520]))  # Output: 2
# print(findPlatform([900, 940, 950, 1100, 1500, 1800], [920, 950, 1020, 1130, 1900, 2000]))  # Output: 3
# print(findPlatform([900, 940], [1000, 1200]))  # Output: 2
# print(findPlatform([800, 810, 820, 830, 840], [830, 840, 850, 860, 870]))  # Output: 5
# print(findPlatform([800, 830, 1000, 1030, 1200, 1500, 1600], [900, 1230, 1030, 1130, 1300, 1530, 1700]))  # Output: 3

# def solve(nums):
#     ptr = 0
#     i = 0
#     c = 0
#     while i < len(nums):
#         i = i + nums[i]
#         if i >= len(nums)-1:
#             return True
#         if nums[i] == 0:
#             return False

# print(solve([2,3,1,1,4]))
# print(solve([1, 2, 3, 4, 5]))
# print(solve([3, 2, 1, 0, 4]))
    
# def solve(haystack,needle):
#     if not needle:
#         return 0
#     if not haystack:
#         return -1
    
#     counter = 0
#     initial = -1
#     for i in range(len(haystack)):
#         if haystack[i] == needle[counter]:
#             if counter == 0:
#                 initial = i
#             counter += 1
#             if counter == len(needle):
#                 return initial
#         else:
#             if counter > 0:
#                 i = initial
#             counter = 0
#             initial = -1
#         i+=1
#     return -1

# hay = "leetcode"
# need = "leet"
# hay1 = "mississippi"
# need1 = "issip"
# # print(solve(hay, need))  # Output: 0
# print(solve(hay1, need1))  # Output: 4


def solve(s):
        ans = ""
        res = []
        for i in range(len(s)):
            if s[i] != " ":
                ans+= s[i]
                if i+1 != len(s) and  s[i+1] == " ":
                    print(i)
                    res.append(ans)
                    ans = "" 
                elif i == len(s)-1:
                    res.append(ans)
        return res

print(solve("   fly me   to   the moon  "))
print(solve("Hello World"))