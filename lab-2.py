# Bubble Sort Full Program

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping happened, array is already sorted
        if not swapped:
            break

    return arr


# Main program
print("---- Bubble Sort Program ----")
arr = list(map(int, input("Enter numbers separated by space: ").split()))

sorted_arr = bubble_sort(arr)

print("Sorted array:", sorted_arr)