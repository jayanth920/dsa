def solve(bills):
    five = 0
    ten = 0

    for i in range(len(bills)):
        if bills[i] == 5:
            five += 1
        elif bills[i] == 10:
            ten += 1
            if five >= 1:
                five -= 1
            else:
                return False
        elif bills[i] == 20:
            if ten >= 1 and five >= 1:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


print(solve([5, 5, 5, 10, 20]))
print(solve([5, 5, 10, 10, 20]))
