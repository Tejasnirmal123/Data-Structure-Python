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

    def print_linked_list(self):
        if self.head is None:
            print("My Linked list is empy")
            return
        itr = self.head
        list = ''
        while itr :
            list += str(itr.data) + '-->'
            itr = itr.next
        print(list)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count = count + 1



l1 = LinkedList()


l1.insert_values([2,3,4,5])

l1.print_linked_list()
l1.remove_at(0)
l1.print_linked_list()
