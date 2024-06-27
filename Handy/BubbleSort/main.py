#Approach 1: Simple Logical
def bubbleSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort([3, 1, 9, 6, 2, 99]))