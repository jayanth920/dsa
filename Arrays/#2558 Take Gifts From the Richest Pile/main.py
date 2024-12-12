from heapq import *
import math


def solve(gifts: list[int], k: int):
        nums = [-num for num in gifts]
        heapify(nums)
        
        while k:
            tmp = math.isqrt(-heappop(nums))
            heappush(nums, -tmp)
            k -= 1
            
        return -sum(nums)
        
print(solve([25,64,9,4,100],4))
print(solve([1,1,1,1],4))
