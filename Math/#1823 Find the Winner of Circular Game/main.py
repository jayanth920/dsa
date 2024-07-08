# 2 Methods - Both O(n)
# Using josephnus formula 
# O(n), constant space as well


# Using josephnus formula 
def findTheWinner(self, n: int, k: int) -> int:
    nums = list(range(n))
    i = 0 
    while len(nums) > 1: 
        i = (i + k-1) % len(nums)
        nums.pop(i)
        return nums[0] + 1
    
# ---------------------------------------------


# O(n), constant space as well - 
from queue import Queue

def findTheWinner(n,k):
    q = Queue()
    c=0
    for i in range(1,n+1):
            q.put(i)
    while(q.qsize() > 1):
        c += 1
        if c % k == 0:
            q.get()
            c = 0
        else:
            front = q.get()
            q.put(front)
    return q.get()
        
    

findTheWinner(5,2)

