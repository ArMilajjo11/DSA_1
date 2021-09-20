class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.temp = None
    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.temp.next = node
        self.temp = node
    def insertatpos(self, data, pos):
        node = Node(data)
        n = self.head
        count = 1
        while n is not None:
            pass







    def print_list(self):
        m = self.head
        while m is not None:
            print(m.data)
            m = m.next
a = Linkedlist()
n = int(input("Enter length: "))
for i in range(n):
    num = int(input("Enter number: "))
    a.push(num)
number = int(input("Enter number you want to put: "))
position = int(input("Enter pos: "))
a.insertatpos(number, position)
a.print_list()







