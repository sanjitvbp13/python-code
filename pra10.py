class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)

def preorder(root):
    if root is None:
        return

    print(root.data, end="")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end="")
    inorder(root.right)

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end="")

if __name__ == "__main__":
    root = Node("1")
    root.left = Node("2")
    root.right = Node("3")
    root.left.left = Node(4)
    root.right.right = Node("5")  
    root.right.left = Node("6")

    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)
