class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertBST(root, element):
    if root is None:
        return Node(element)
    
    if element < root.data:
        root.left = insertBST(root.left, element)
    else:
        root.right = insertBST(root.right, element)
    
    return root

def InOrder(root):
    if root is None:
        return
    
    InOrder(root.left)
    print(root.data)
    InOrder(root.right)

if __name__ == "__main__":
    list = [10, 5, 15, 2, 7, 12, 20]
    root = None
    for num in list:
        root = insertBST(root, num)
    InOrder(root)
