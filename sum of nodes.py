class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
list = []
def sumofNodes(root):
    if root is None:
        return
    sumofNodes(root.left)
    list.append(root.data)
    sumofNodes(root.right)

    return list
if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    list1 = sumofNodes(root)
    print(sum(list1))