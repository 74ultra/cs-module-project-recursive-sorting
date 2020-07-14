# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] > target:
            return binary_search(arr, target, start, middle_index-1)
        elif arr[middle_index] < target:
            return binary_search(arr, target, middle_index+1, end)
    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    if arr[0] < arr[len(arr)-1]:
        while high >= low:
            midpoint = (low + high)//2
            if arr[midpoint] == target:
                return midpoint
            elif arr[midpoint] > target:
                high = midpoint - 1
            elif arr[midpoint] < target:
                low = midpoint + 1
        return -1
    elif arr[0] > arr[len(arr)-1]:
        while high >= low:
            midpoint = (low + high)//2
            if arr[midpoint] == target:
                return midpoint
            elif arr[midpoint] < target:
                high = midpoint - 1
            elif arr[midpoint] > target:
                low = midpoint + 1
        return -1


# xer = [3, 4, 5, 7, 8, 9, 19, 21, 31, 36]
# zer = [36, 31, 21, 19, 9, 8, 7, 5, 4, 3]

# print(agnostic_binary_search(xer, 361))
