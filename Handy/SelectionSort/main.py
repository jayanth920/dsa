def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage:
array = [64, 25, 12, 22, 11]
print("Sorted array:", selection_sort(array))  # Output: [11, 12, 22, 25, 64]
