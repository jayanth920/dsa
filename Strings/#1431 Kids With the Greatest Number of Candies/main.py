def solve(candies, extraCandies):
    # SLOW ASF IDIOT
    # res = []
    # for i in range(len(candies)):
    #     arr: list = candies[:]
    #     temp = arr[i]+ extraCandies
    #     arr[i] = arr[i]+extraCandies
    #     # print("i: ",i," temp: ",temp," arr:",arr)
    #     arr.sort(reverse=True)
    #     # print("SortedArr: ",arr)
    #     if arr[0] == temp:
    #         res.append(True)
    #     else:
    #         res.append(False)
    # return res
    
    res = []
    maxCandies = max(candies)
    for i in range(len(candies)):
        res.append(candies[i] + extraCandies >= maxCandies)
    return res
            
        
    
    
print(solve([2,3,5,1,3], 3))
print(solve([4,2,1,1,2], 1))
print(solve([12,1,12], 10))