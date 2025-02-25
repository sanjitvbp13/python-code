class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size  # Array to store tree nodes

    def add(self, key, index):
        """Add a node at a specific index."""
        if index < len(self.tree):
            self.tree[index] = key
        else:
            print("Index out of bounds!")

    def get_left_child(self, index):
        """Get the left child of a node."""
        left_index = 2 * index + 1
        return self.tree[left_index] if left_index < len(self.tree) else None

    def get_right_child(self, index):
        """Get the right child of a node."""
        right_index = 2 * index + 2
        return self.tree[right_index] if right_index < len(self.tree) else None

    def get_parent(self, index):
        """Get the parent of a node."""
        if index == 0:
            return None  # Root node has no parent
        parent_index = (index - 1) // 2
        return self.tree[parent_index]

    def display(self):
        """Print the tree as an array."""
        print(self.tree)

# Example usage
tree = BinaryTree(7)
tree.add(1, 0)  # Root
tree.add(2, 1)  # Left child of root
tree.add(3, 2)  # Right child of root
tree.add(4, 3)  # Left child of node at index 1
tree.add(5, 4)  # Right child of node at index 1

tree.display()

print("Left child of root:", tree.get_left_child(0))
print("Right child of root:", tree.get_right_child(0))
print("Parent of node at index 3:", tree.get_parent(3))
