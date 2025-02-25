#wtite a program to traverse a linked list.

class node:
    def __init__(self, data):  
        self.data = data
        self.next = None

if __name__ == "__main__": 
    head = node(1)
    head.next = node(3)
    head.next.next = node(5)
    head.next.next.next = node(7)
    head.next.next.next.next = node(9)
    #temp = head
    fast=head
    slow=head
    while fast.next:  
        fast = fast.next.next
        slow = slow.next
    print("middle of linked list:", slow.data)  

