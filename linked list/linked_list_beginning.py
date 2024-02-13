class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print_linked_list(self):
        if self.head is None:
            print("My Linked list is empy")
            return
        itr = self.head
        list = ''
        while itr :
            list += str(itr.data) + '-->'
            itr = itr.next     # head will become the next node 
        print(list)

    

    
l1 = LinkedList()
l1.insert_at_end(2)
l1.insert_at_end(5)



l1.print_linked_list()
