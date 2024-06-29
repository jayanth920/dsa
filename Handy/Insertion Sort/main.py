def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

arr = [9, 4, 3, 7, 5, 1]
print("Sorted Array:", insertion_sort(arr))

#--------------------- Recursive -------------------------
def recursive_insertion_sort(arr, i=1):
    if i >= len(arr):
        return arr
    
    j = i
    while j > 0 and arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
    
    return recursive_insertion_sort(arr, i + 1)

arr = [9, 4, 3, 7, 5, 1]
print("Sorted Array:", recursive_insertion_sort(arr))
