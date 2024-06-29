# O(n)
# def armstrong(n):
#     new = str(n)
#     sum = 0
#     for i in range(len(new)):
#         sum = sum + int(new[i])**3
#     print(sum)
# armstrong(153)


 #O(logn + 1)

def armstrong(n):
    num = n
    l = len(str(n))
    sum = 0
    while(num>0):
        ld = num % 10
        sum = sum + ld**l
        num = n//10
    return sum
print(armstrong(234))

