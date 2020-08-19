# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    while start <= end:
        middle = (start + end) // 2

        if target < arr[middle]:
            return binary_search(arr, target, start, (middle - 1))
        elif target > arr[middle]:
            return binary_search(arr, target, (middle + 1), end)
        else:
            return middle

    return -1  # not found


    # if end >= start:
    #     mid = start + (end-1) // 2
    #     if arr[mid] == target:
    #         return mid
    #     elif arr[mid] > target:
    #         return binary_search(arr, target, start, mid - 1)
    #     else:
    #         return binary_search(arr, target, mid + 1, end)
    # else:
    #     return -1

        # middle = start + end // 2
        # if len(arr) == 0:
        #     return -1

        # if arr[middle] == target:
        #     return middle

        # else:
        #     if target > arr[middle]:
        #         low = middle -1

        # elif target < arr[middle]:
        #     high = middle + 1

        # return binary_search_recursive(arr, target, high, low)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):

    low = 0
    high = len(arr) -1

    # while low < high:
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        high = mid - 1
    elif target > arr[mid]:
        low = mid + 1
    else:
        low > high

    return -1