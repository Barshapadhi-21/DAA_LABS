# Selection Sort Full Program

def selection_sort(arr):
    n = len(arr)

    # Traverse through all elements
    for i in range(n):
        min_index = i

        # Find the minimum element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Main program
print("---- Selection Sort Program ----")
arr = list(map(int, input("Enter numbers separated by space: ").split()))

sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr)

arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]
    print("After pass", i + 1, ":", arr)

print("Final sorted array:", arr)