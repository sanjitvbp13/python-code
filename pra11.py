class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
list=[]

def InOrder(root):
    if root is None:
        return
    InOrder(root.left)
    list.append(root.data)
    InOrder(root.right)
    return list
    
if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(6)
    root1.right.left = Node(7)
    root2 = Node(1)
    root2.left = Node(3)
    root2.right = Node(2)
    root2.left.left = Node(7)
    root2.left.right = Node(6)
    root2.right.right = Node(5)
    root2.right.left = Node(4)


    list1=[]
    list2=[]
    list1=(InOrder(root1)).copy()
    list.clear()
    list2=(InOrder(root2)).copy()
    list2.reverse()

    if list1==list2:
        print ("tree are mirror")
    else:
        print ("tree are not mirror")
    