import random
import timeit

# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Check if left child exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # Check if right child exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root
        heapify(arr, n, largest)

# Main function to perform heap sort
def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Input array size from the user
array_size = int(input("Enter the size of the input array: "))

# Generate random elements
input_array = [random.randint(1, 1000) for _ in range(array_size)]

# Print the unsorted array
print("Unsorted Array:", input_array)

# Measure the execution time for sorting
start_time = timeit.default_timer()
heapSort(input_array)
end_time = timeit.default_timer()
execution_time = (end_time - start_time)

# Print the sorted array
print("Sorted Array:", input_array)

# Print the execution time
print("Execution time for sorting:", end_time - start_time, "seconds")
