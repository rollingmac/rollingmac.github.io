#Yeung Pok
#20965361
import random
import math

# Create the sorted array
array = list(range(1000000))

# 1. Binary Search with step count
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if array[mid] == target:
            return mid, steps
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

# 2. Jump Search with step count
def jump_search(array, target):
    n = len(array)
    step = int(math.sqrt(n))
    prev = 0
    steps = 0

    while prev < n and array[min(step, n)-1] < target:
        steps += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, steps

    for i in range(prev, min(step, n)):
        steps += 1
        if array[i] == target:
            return i, steps
    return -1, steps

# 3. Exponential Search with step count
def binary_search_exponential(array, low, high, target):
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        steps += 1
        if array[mid] == target:
            return mid, steps
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

def exponential_search(array, target):
    if array[0] == target:
        return 0, 1  # 1 step for the first check
    bound = 1
    steps = 1  # Initial check
    while bound < len(array) and array[bound] <= target:
        steps += 1
        bound *= 2
    return binary_search_exponential(array, bound // 2, min(bound, len(array) - 1), target)

# 4. Ternary Search with step count
def ternary_search(array, target, low, high):
    steps = 0
    while high >= low:
        steps += 1
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if array[mid1] == target:
            return mid1, steps
        if array[mid2] == target:
            return mid2, steps
        if target < array[mid1]:
            high = mid1 - 1
        elif target > array[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1, steps

# Simulate the search for a random target
target = random.randint(0, 999999)


# Run each search algorithm and count steps
binary_result, binary_steps = binary_search(array, target)
jump_result, jump_steps = jump_search(array, target)
exponential_result, exponential_steps = exponential_search(array, target)
ternary_result, ternary_steps = ternary_search(array, target, 0, len(array) - 1)

# Print the results
print(f"Binary Search Steps: {binary_steps}, Result: {binary_result}")
print(f"Jump Search Steps: {jump_steps}, Result: {jump_result}")
print(f"Exponential Search Steps: {exponential_steps}, Result: {exponential_result}")
print(f"Ternary Search Steps: {ternary_steps}, Result: {ternary_result}")
