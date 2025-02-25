class Node:
    def __init__(root, data):
        root.data = data
        root.left = None
        root.right = None

    def InOrder(root):
        if root is None:
            return
        Node.InOrder(root.left)
        print(root.data, end="")
        Node.InOrder(root.right)

    def mirrorImage(root):
        if root is None:
            return  
        Node.mirrorImage(root.left)
        Node.mirrorImage(root.right)
        temp = root.right
        root.right = root.left
        root.left = temp
        return root
if __name__ == "__main__":
    root = Node("1")
    root.left = Node("2")
    root.right = Node("3")
    root.left.left = Node("4")
    root.left.right = Node("5")
    root.right.right = Node("6")
    root.right.left = Node("7")

    print("Tree InOrder: ", end="")
    Node.InOrder(root)
    print("\nMirror Tree InOrder:", end="")
    Node.InOrder(Node.mirrorImage(root)) 
    