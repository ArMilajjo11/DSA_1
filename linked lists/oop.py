class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = node
            temp.next = self.head
            self.head = temp
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next
    def delete_last(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None




