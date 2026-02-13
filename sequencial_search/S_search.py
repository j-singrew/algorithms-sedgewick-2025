

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None




def Get(find_key:int):
    node1 = Node(15)
    node2 = Node(3)
    node3 = Node(17)
    node4 = Node(90)

    node1.next = node2
    node2.next = node3
    node3.next = node4  

    head = node1 

    current = head
    while current:
        if current.value ==  find_key:
            return "found node"
        current = current.next
    return "no next_found"
        

def put(data:int):
    node1 = Node(15)
    node2 = Node(3)
    node3 = Node(17)
    node4 = Node(90)

    node1.next = node2
    node2.next = node3
    node3.next = node4  

    head = node1 

    current = head

    while current:
        if current.value ==  data:
                current.value = data
                return current.value,current.next
        current = current.next
        
    new_node = Node(data)
    return new_node.value,new_node.next













