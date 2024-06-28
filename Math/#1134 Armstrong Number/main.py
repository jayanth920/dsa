def armstrong(n):
    new = str(n)
    sum = 0
    for i in range(len(new)):
        sum = sum + int(new[i])**3
    print(sum)
armstrong(153)