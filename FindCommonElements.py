# Give three SORTED arrays in non-decreasing order, print all common elements in these arrays

# Find the insersection of two arrays
# Store the intersection in a temp array
# Find the intersection of the third array and temp array


def FindCommonElements(arr1, arr2, arr3, n1, n2, n3):
    i, j, k = 0, 0, 0

    while (i < n1 and j < n2 and k < n3):
        if (arr1[i] == arr2[j] and arr2[j] == arr3[k]):
            print (arr1[i])
            i += 1
            j += 1
            k += 1

        elif arr1[i] > arr2[j]:
            i += 1
        
        elif arr2[j] < arr3[k]:
            j += 1
        
        else:
            k += 1


arr1 = [1, 9, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)

# function call
print("Common Elements:")
FindCommonElements(arr1, arr2, arr3, n1, n2, n3)