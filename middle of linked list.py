#write a program to find the middle of a linked list
class node:
    def __init__(self, data):  
        self.data = data
        self.next = None

if __name__ == "__main__": 
    head = node(1)
    head.next = node(3)
    head.next.next = node(5)
    head.next.next.next = node(7)
    temp = head
    while temp:  
        print(temp.data, end="->")
        temp = temp.next
    print("null")  
middle_node= findMiddleNode(head)
print("The Middle Node is ",end='')
print(middle_node.data,"\n")


