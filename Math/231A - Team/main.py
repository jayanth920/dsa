n = int(input()) 
c = 0 

problems = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    total = sum(problems[i]) 
    if total >= 2:
        c += 1

print(c)
