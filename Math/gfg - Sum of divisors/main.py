import math
def sumOfDivisors(N):
    sum = 0
    sq = math.floor(math.sqrt(N))
    print(sq)
    li = []
    for i in range(1,sq+1):
        if(N % i == 0):
            li.append(i)
            if(i != N//i):
                li.append(N//i)
    print(li)
sumOfDivisors(5)