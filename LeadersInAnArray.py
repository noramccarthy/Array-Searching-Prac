# Write a program to print all the LEADERS in the array
# An element is a leader if it is greater than all the elements to its right
# The rightmost element is always a leader

def printLeaders(arr, n):
    max_from_right = arr[n-1] # last element is always a leader
    print(max_from_right)

    for i in range(n-2, -1, -1): # start, stop, step
        if arr[i] > max_from_right:
            print(arr[i])
            max_from_right = arr[i]

arr = [16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))