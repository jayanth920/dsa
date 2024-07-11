num = int(input())
arr = []
final = []
for i in range(num):
    word = input()
    arr.append(word)
 
for i,word in enumerate(arr):
    length = len(word)
    if(length <=10 ):
        final.append(word)
    else:
        new = str(word[0]) + str(length-2) + str(word[length-1])
        final.append(new)
 
for i,word in enumerate(final):
    print(word)
