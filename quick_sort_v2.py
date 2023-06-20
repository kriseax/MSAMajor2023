def quicksort_iterative(arr):
    # Create a stack to simulate the recursive calls
    stack = []
    #Place list partitions on the stack
    stack.append((0, len(arr) - 1))

    while stack:
        #Get the next partition to process
        low, high = stack.pop()

        # Partition the array. Find the pivot index for the list
        pivot_index = partition(arr, low, high)

        # If there are elements on the left side of the pivot, push them to the stack
        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))

        # If there are elements on the right side of the pivot, push them to the stack
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot, swap it with the element at the border (i+1)
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at the border
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    #arr = [7, 2, 1, 6, 8, 5, 3, 4]
    arr = [40, 80, 10, 90, 30, 50, 70]
    quicksort_iterative(arr)
    print(arr)

main()
