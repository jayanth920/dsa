n, k = map(int,input().split())
scores = list(map(int, input().split()))

c=0
max = scores[k-1]

for i in range(n):
    if scores[i] > 0 and scores[i] >= max:
        c+=1
print(c)