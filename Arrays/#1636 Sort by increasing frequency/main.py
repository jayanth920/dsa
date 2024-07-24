from collections import Counter

def frequencySort(nums):
    freq = Counter(nums)
    sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
    return sorted_nums

nums1 = [1, 1, 2, 2, 2, 3]
print(frequencySort(nums1)) # Output: [3, 1, 1, 2, 2, 2]

nums2 = [2, 3, 1, 3, 2]
print(frequencySort(nums2)) # Output: [1, 3, 3, 2, 2]

nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(frequencySort(nums3)) # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]