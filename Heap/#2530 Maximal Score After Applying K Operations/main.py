import math,heapq
def solve(nums,k):
        score = 0
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        while k:
            t = -heapq.heappop(max_heap)
            score += t
            k-=1 
            heapq.heappush(max_heap,-math.ceil(t/3))
        return score
    
print(solve([1,10,3,3,3],3))
print(solve([10,10,10,10,10],5))