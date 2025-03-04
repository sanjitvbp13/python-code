class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def MaxDepth(root):
  if root is None: return 0
  else:
    return max(MaxDepth(root.left), MaxDepth(root.right)) + 1


if __name__ == "__main__":
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.left = Node(6)
  root.right.right = Node(7)
  root.right.left.left = Node(8)
  root.right.right.right = Node(9)
  root.right.right.right.left = Node(10)
  print(MaxDepth(root))
