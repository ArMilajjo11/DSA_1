class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None
    def insert(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.temp.next = node
        self.temp = node

    def print_list(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

n = int(input("Enter number of elements: "))
ll1  = LinkedList()
for i in range(n):
    data = int(input("Enter element: "))
    ll1.insert(data)
ll1.print_list()
