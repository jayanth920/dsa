import math

def prime(n):
    count = 0
    for i in range(1,int(math.sqrt(n)+1)):
        if(n%i == 0):
            count = count + 1
            if(n//i != i):
                count = count + 1
                # print(i,count)
                
    if count == 2:
        # print(count)
        return True
    else: 
        # print(count)
        return False
    
print(prime(10))