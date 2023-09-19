from typing import List

# Given a sequence arr[] of size n
# Write a function that returns an equilibirum index (if any) or -1 if no equilibrium index exists
# The equilibrium index is an index where the sum of elements at lower indexes == sum of elements at higher indexes

# ****************************************************************************************************
# Using Array-Sum
    # Get total sum of array first
    # Iterate through the array and keep updating the left sum which is initalized as 0
    # In the loop, get the right sum by subtracting the elements one by one

def arraySum(arr):
    left_sum = 0
    total_sum = sum(arr) # finding the sum of whole array

    for i, num in enumerate(arr):
        total_sum = total_sum - num # update the sum to get the right sum (sum is now right sum)

        if left_sum == total_sum: # if left sum = sum, return index
            return i
        
        left_sum = left_sum + num # update left sum for next iteration
    
    return -1 # If no equilibrium index found, return -1


arr = [-7, 1, 5, 2, -4, 3, 0]
# Function call
print('Equilibrium index in arraySum:', arraySum(arr))

# TC: O(N)
# AS: O(1)

# ****************************************************************************************************

# Using Prefix-Sum
    # Take 2 prefix sums of the array (one from front, one from back)
    # Run a loop from 1 to N
    # Check if at any point the prefix sum from front == prefix sum from back
    # Return index else return -1

def prefixSum(array):
    left_sum = []
    right_sum = []

    # iterate from 0 to len(arr)
    for i in range(len(array)):
        # if i is not 0
        if(i):
            left_sum.append(left_sum[i-1] + array[i])
            right_sum.append(right_sum[i-1] + array[len(arr) -1 -i])
        else:
            left_sum.append(array[i])
            right_sum.append(array[len(arr) -1])

    # iterate from 0 to len(arr)
    for i in range(len(array)):
        if(left_sum[i] == right_sum[len(array) - 1 -i]):
            return(i)
        
    return -1

array = [-7, 1, 5, 2, -4, 3, 0]

# Function call
print('Eqilibrium index of prefixSum is ', prefixSum(array))

# TC: O(N)
# AS: O(N)

# ****************************************************************************************************
# Using two pointers
#   Use two pointers (left and right) to keep track of the sum of elements to the left and right of the pivot index
#   Initlaize left pointer to 0, pivot to 0, and right pointer to the sum of all elements minus the first element
#   Pivot index is incremented until the left pointer = right pointer, or until the pivot index is the last index

# In each iteration,
#   the pivot index is inremented,
#   the right poiter is decremented by the element at the current pivot index,
#   left pointer is incremented by value of element at previous pivot index


def pivotIndex(nums: List[int]) -> int:
    left, pivot, right = 0, 0, sum(nums)-nums[0]
    while pivot < len(nums)-1 and right != left:
        pivot += 1
        right -= nums[pivot]
        left += nums[pivot-1]

    return pivot if left == right else -1


nums = [1, 7, 3, 6, 5, 6]
print("Equilbrium Index of two pointers:", pivotIndex(nums))

