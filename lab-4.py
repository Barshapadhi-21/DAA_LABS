# Sequential Search (Linear Search) Full Program

def sequential_search(arr, key):
    # Traverse each element
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # return index if found
    return -1   # return -1 if not found


# Main program
def main():
    print("---- Sequential Search Program ----")

    # Taking input
    arr = list(map(int, input("Enter elements separated by space: ").split()))
    key = int(input("Enter element to search: "))

    # Function call
    result = sequential_search(arr, key)

    # Output result
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found")


# Run program
if __name__ == "__main__":
    main()