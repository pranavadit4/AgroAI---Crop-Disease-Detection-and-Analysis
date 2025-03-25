#binary search tree

'''class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class BST:
    def create(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.create(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        elif data > node.data:
            node.right = self.insert(node.right,data)
        return node

def Inorder(self,node):
    if node is not None:
        self.Inorder(node,left)
        print(node.data)
        self.Inorder(node.right)

tree = BST()
root = tree.create(8)
a = int(input("Enter n no of nodes you neeed : "))
for i in range(a):
    tree.insert(root,int(input()))
print("Inorder: ")
tree.Inorder(root)'''


#missing number in array without looping statements

'''def find_missing(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
    
arr = list(map(int, input("Enter numbers: ").split()))
print("Missing number:", find_missing(arr))'''


'''from itertools import permutations

def is_magic_square(matrix):
    return (
        sum(matrix[0]) == sum(matrix[1]) == sum(matrix[2]) == 15 and
        sum(matrix[i][0] for i in range(3)) ==
        sum(matrix[i][1] for i in range(3)) ==
        sum(matrix[i][2] for i in range(3)) == 15 and
        sum(matrix[i][i] for i in range(3)) == 15 and
        sum(matrix[i][2-i] for i in range(3)) == 15
    )

def generate_magic_square():
    for perm in permutations(range(1, 10)):
        matrix = [list(perm[i:i+3]) for i in range(0, 9, 3)]
        if is_magic_square(matrix):
            return matrix

def print_magic_square(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    magic_square = generate_magic_square()
    print_magic_square(magic_square)'''




