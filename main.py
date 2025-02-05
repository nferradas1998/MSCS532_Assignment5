import random
import time
import deterministic_quicksort
import randomized_quicksort


# method to generate a randomized array, where n is the size and m the max possible value
def generate_random_array(n, m): 
    return [random.randint(0, m) for _ in range(n)]

# method to generate a sorted array of size n
def generate_sorted_array(n):
    return list(range(n))

# method to generate a reverse-sorted array of size n
def generate_reverse_sorted_array(n):
    return list(range(n, 0, -1))

def get_performance(func, arr):
    start_time = time.time()  # start
    func(arr)  # Call the function
    end_time = time.time()  # end
    return (end_time - start_time)

arr = generate_random_array(10000, 12000)
time_taken_deterministic = get_performance(deterministic_quicksort.quicksort, arr)
time_taken_randomized = get_performance(randomized_quicksort.quicksort, arr)

print("Randomize Array performance: \n Deterministic Quicksort: ", time_taken_deterministic, "\n Randomized Quicksort: ", time_taken_randomized)


arr = generate_sorted_array(10000)
time_taken_deterministic = get_performance(deterministic_quicksort.quicksort, arr)
time_taken_randomized = get_performance(randomized_quicksort.quicksort, arr)

print("Sorterd Array performance: \n Deterministic Quicksort: ", time_taken_deterministic, "\n Randomized Quicksort: ", time_taken_randomized)

arr = generate_reverse_sorted_array(10000)
time_taken_deterministic = get_performance(deterministic_quicksort.quicksort, arr)
time_taken_randomized = get_performance(randomized_quicksort.quicksort, arr)

print("Reverse-sorted Array performance: \n Deterministic Quicksort: ", time_taken_deterministic, "\n Randomized Quicksort: ", time_taken_randomized)

