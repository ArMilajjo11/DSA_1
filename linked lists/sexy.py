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

    def insert_last(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.temp.next = node
        self.temp = node

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_pos(self,pos):
        pass


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


a = LinkedList()

