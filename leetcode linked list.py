class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_nodes(head):
    temp = head
    while temp and temp.next:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next
    return head

if __name__ == "__main__":
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(6)
    head1.next.next.next = Node(7)
    head1.next.next.next.next = Node(8)
    head2 = Node(3)
    head2.next = Node(4)
    head2.next.next = Node(5)
    head2.next.next.next = head1.next.next
    head2.next.next.next.next = Node(7)
    head2.next.next.next.next.next = Node(8)

    head1 = swap_nodes(head1)
    temp = head1
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
