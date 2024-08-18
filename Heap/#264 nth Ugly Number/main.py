import heapq

# SOLUTION 1 - BEST -  Fast but same memory
def solve(n):
    # Initialize a min-heap
    heap = [1]
    # Set to track the numbers we have seen and avoid duplicates
    seen = {1}
    
    # Iterate n times to find the nth ugly number
    for _ in range(n):
        # Get the smallest number from the heap
        ugly = heapq.heappop(heap)
        
        # Generate new ugly numbers by multiplying with 2, 3, and 5
        for factor in [2, 3, 5]:
            new_ugly = ugly * factor
            if new_ugly not in seen:
                seen.add(new_ugly)
                heapq.heappush(heap, new_ugly)
    
    # After the loop, `ugly` will be the nth ugly number
    return ugly

# -------------------------------------------------------------------

# SOLUTION 2 

# USING ARRAYS - SLOWER BUT SAME MEMORY or lesser
def solve(n):
        ugly_numbers = [1]  # Start with the first ugly number
        
        for _ in range(1,n):  # We need to find n ugly numbers
            min_ugly = ugly_numbers.pop(0)  # Pop the smallest ugly number
            # Generate new ugly numbers and add them back to the list
            for factor in [2, 3, 5]:
                new_ugly = min_ugly * factor
                if new_ugly not in ugly_numbers:
                    ugly_numbers.append(new_ugly)
            ugly_numbers.sort()  # Sort the list to bring the smallest number to the front
        
        return ugly_numbers[0]  # The nth ugly number is now the first in the list

    
print(solve(10))
print(solve(3))
print(solve(11))
print(solve(1))
# print(solve(103))