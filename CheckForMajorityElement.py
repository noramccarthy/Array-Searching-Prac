# Given an array arr of N elements, a majority element in an array of size N is an element that appears more than N/2 times

# Take in an array, array's size (n), and a nubmer to be searched (x)
# Return true if x is a majority element(present more than n/2 times)

def isMajority(arr, n, x):
    
    lastIndex = (n//2 + 1) if n % 2 == 0 else (n//2) # get last index, consider odd and even numbers
    print("Last index:", lastIndex)
    
    for i in range(lastIndex): # search for first occurence of x
        if arr[i] == x and arr[i + n//2] == x: # check if x is present and if it is present more than n/2 times
            return 1

arr = [1, 2, 3, 4, 4, 4, 4]
n = len(arr) # 7
x = 4

if (isMajority(arr, n, x)):
    print ("% d appears more than % d times in arr[]" %(x, n//2))
else:
    print ("% d does not appear more than % d times in arr[]" %(x, n//2))