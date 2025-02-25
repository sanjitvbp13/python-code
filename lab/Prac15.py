class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
list = []
def InOrder(root):
    if root is None:
        return
    InOrder(root.left)
    list.append(root.data)
    InOrder(root.right)

    return list
def ISVALID(list1):
    if list1 == sorted(list1):
        return True
    else:
        return False
if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    list1 = InOrder(root)
    print(ISVALID(list1))