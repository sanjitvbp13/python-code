class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    list1 = []
    temp1 = head1
    temp2 = head2
    
    while temp1:
        list1.append(temp1.data)
        temp1 = temp1.next
    
    while temp2:
        if temp2.data in list1:
            print("Merge Point: ", temp2.data)
            break
        temp2 = temp2.next
