class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
if _name_ == "_main_":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    temp = head
    while temp and temp.next:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("NULL")
