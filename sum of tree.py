class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root,sum):
    if root is None:
        return sum

    
    sum = inorder(root.left,sum)
    sum  += root.data
    print(root.data)
    sum = inorder(root.right,sum)
    return sum

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)  
    root.right.left = Node(6)
    root.right.left.right = Node(7)
    total_sum = inorder(root, 0)
    print("Total sum:", total_sum)