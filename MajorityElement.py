# Find the majority element in the array
# A majority element is an element that appears more than n/2 times (and hence there is at most one such element)

# Use Binary Search Tree! not nested for loop

# Create a binary search tree, traverse the array and insert the element into the BST
# If the same element is entered in the BST, the frequency of the node is increased
# If the max frequency of any node is > half the size of the array, then perform an inorder traversal and find the node
# Else print no majority element

# class for creating node
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1 # num of times data is inserted in class for BST


# class for BST
class BST():
    def __init__(self):
        self.root = None # initalizes tree with None root

    # function inserts node as per BST rule
    def insert(self, data, n):
        out = None
        if (self.root  == None):
            self.root = Node(data)
        else:
            out = self.insertNode(self.root, data ,n)
        return out
    
    def insertNode(self, currentNode, data, n):
        if (currentNode.data == data):
            currentNode.count += 1
            if (currentNode.count > n//2):
                return currentNode.data
            else:
                return None
        elif (currentNode.data < data):
            if (currentNode.right):
                self.insertNode(currentNode.right, data, n)
            else:
                currentNode.right = Node(data)
        elif (currentNode.data > data):
            if (currentNode.left):
                self.insertNode(currentNode.left, data, n)
            else:
                currentNode.left = Node(data)

# declaring an array
arr = [3, 2, 3]
n = len(arr)

# declaring None tree
tree = BST()
flag = 0
for i in range(n):
    out = tree.insert(arr[i], n)
    if (out != None):
        print(arr[i])
        flag = 1
        break
if (flag == 0):
    print("No Majority Element")