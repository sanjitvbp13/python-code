class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def LevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].data,end=" ")
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__=="__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(20)
    LevelOrder(root)