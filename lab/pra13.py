class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LCA(root, n1, n2): 
    if root is None:
        return None
    if root.data == n1 or root.data == n2:  # Use equality operator instead of "is"
        return root
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)

    if left is None:
        return right
    if right is None:
        return left
    else:
        return root

if __name__ == "__main__":
    root = TreeNode(1) 
    root.left = TreeNode(2) 
    root.right = TreeNode(3) 
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5) 
    root.right.left = TreeNode(6) 
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(8)

    n1 = int(input("Enter a number:"))
    n2 = int(input("Enter another number:"))

    result = LCA(root, n1, n2)
    if result:
        print("Lowest Common Ancestor:", result.data)
    else:
        print("One or both nodes not found in the tree.")
