class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None

if __name__ == "__main__":  
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(5)
    
    head2 = Node(2)
    head2.next = Node(4)
    head2.next.next = Node(6)
    
    v = []
    temp1 = head
    temp2 = head2
    
    while temp1:
        v.append(temp1.data)
        temp1 = temp1.next
    
    while temp2:
        v.append(temp2.data)
        temp2 = temp2.next
    
    v.sort()
    
    dummyNode = Node(-1)
    temp = dummyNode
    
    for num in v:
        temp.next = Node(num)
        temp = temp.next
    
    temp = dummyNode.next
    
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    
    print("null")
