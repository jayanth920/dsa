n = int(input())
x = 0
for _ in range(n):
    statement = input().strip()
    if '++' in statement:
        x += 1
    elif '--' in statement:
        x -= 1
print(x)
