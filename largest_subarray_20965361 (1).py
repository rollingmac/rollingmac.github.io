from array import array


from array import array

def find_largest_subarray_sum(arr):
    # Handle empty array case
    if not arr:
        return 0

    max_sum = current_sum = arr[0]  # Initialize with the first element

    for num in arr[1:]:  # Iterate over the array starting from the second element
        # Update current_sum: either start a new subarray or continue the existing one
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum  # Return the maximum subarray sum

# Example usage
arr = array('i', [-2, 1, -3, 4, -1, 2, 1, -5, 4])
max_sum = find_largest_subarray_sum(arr)
print(max_sum)  # Output: 6
print(find_largest_subarray_sum(array('i', [])))  # Output: 0 (empty array)
print(find_largest_subarray_sum(array('i', [-1, -2, -3])))  # Output: -1 (all negative)
