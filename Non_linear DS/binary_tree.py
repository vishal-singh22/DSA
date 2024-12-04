class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Inorder Traversal: ")
inorder(root)
print("\nPreorder Traversal: ")
preorder(root)
print("\nPostorder Traversal: ")
postorder(root)
