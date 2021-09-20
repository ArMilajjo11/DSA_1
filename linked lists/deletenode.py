class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def delete_pos(self, pos):
        if self.head is None:
            print("List is empty")
        else:
            count = 0
            n = self.head
            while True:
                if count is pos:
                    previous.next = n.next
                    n.next = None
                    break
                previous = n
                n = n.next
                count += 1

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.temp.next = node
        self.temp = node

    def print_list(self):
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.next

a = LinkedList()
n = int(input("Enter number of elements "))
for i in range(n):
    item = int(input("Enter element "))
    a.push(item)

a.print_list()
pos = int(input("Enter position "))
a.delete_pos(pos)
a.print_list()
