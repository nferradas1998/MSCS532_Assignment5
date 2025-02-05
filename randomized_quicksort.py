import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Select a random number for the pivot index
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with last element
    pivot = arr[high]  # Use the last element as pivot after swap
    i = low - 1  # Pointer for the smaller element
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1  # Move the pointer forward
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    # Place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the pivot index


def quicksort(arr):
    if len(arr) <= 1:
        return arr  # we just return the array since we can consider it sorted
    
    stack = [(0, len(arr) - 1)]  # Stack to store indexes
    
    while stack:
        low, high = stack.pop()  # Pop the top range
        
        if low < high:
            pivot_index = partition(arr, low, high)  # call the partition function 
            
            # Push left and right subarrays onto the stack
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high)) 
    
    return arr  # Return the sorted array

