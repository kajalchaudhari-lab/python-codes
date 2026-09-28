class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

       
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        
        temp.next = new_node
        new_node.prev = temp
    
    def display_forward(self):
        temp = self.head
       

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

    print("None")
    
    def display_backward(self):
        if self.head is None:
            print("empty")
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            
        while temp is not None:
            print(temp.data,end="<->")
            temp = temp.prev
            
        print("None")
            



dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(40)
dll.insert_end(30)
dll.display_forward()
dll.display_backward()
