# if just searching once, maybe don't sort
# if searching a lot, then maybe go ahead and sort

# STRETCH: implement Linear Search				
# Return index
def linear_search(arr, target):
  ## iterate over the entire array
    for index in range(len(arr)):
    ## compare each element with the target
      if arr[index] == target:
      ## when you find target, return index
        return index
    return -1   # not found


# .index()
## probably iterating over the array, like a for-loop
## stops and returns first instance of target

# STRETCH: write an iterative implementation of Binary Search 
# remember the array is already sorted

# // or use round() or math.floor()
# math.ceil()
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  # Keep track of upper and lower bounds
  low = 0
  high = len(arr)-1

    # stop if we have no values left
  while low <= high:
    # find the middle of those bounds
    middle = (low + high) // 2 # make sure it's an int --> index

      # check if this is our target
    if target == arr[middle]:
      return middle
    # Check if the target is above or below the middle
    # Move upper or lower bound to the middle (to cut array in half)
    elif target > arr[middle]:
      low = middle - 1
    elif target < arr[middle]:
      high = middle + 1

  return -1 # not found


# move toward the base case
## pass high and low as params

def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)/2

  if len(arr) == 0:
    return -1 # array empty

  elif low > high:
    return -1 # not found

  elif arr[middle] == target:
    return middle

  else:
    if target < arr[middle]:
      high = middle-1 # eliminate RHS
    else:      
      low = middle+1 # eliminate LHS
    return binary_search_recursive(arr, target, low, high)

def binary_search_recursive_extra(arr, target):
  
  low = 0
  high = len(arr) - 1
  middle = (low+high)//2

  # Base case
  ## if array is empty
  if len(arr) == 0:
    return -1 # array empty

  if arr[middle] == target:
    return middle

  else: 
    # Check if the target is above or below the middle
    if target > arr[middle]:
      one_half = arr[middle:high + 1]
      
    elif target < arr[middle]:
      one_half = arr[low:middle + 1]

    return binary_search_recursive(one_half, target)