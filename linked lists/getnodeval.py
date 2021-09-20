class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
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

def getNode(head, pos):
    current = head
    prev = None
    following = current.next
    while current is not None:
        current.next = prev
        prev = current
        current = following
        if following is not None:
            following = following.next
    head = prev
    count = 0
    n = head
    while n is not None:
        if count == pos:
            return n.data
        else:
            n = n.next
            count = count +1

test = int(input("Enter no. of test cases: "))
for i in range(test):
    a = Linked_list()
    l = int(input("Enter length of list: "))
    for j in range(l):
        num = int(input("Enter no.: "))
        a.push(num)
    pos = int(input("Enter pos: "))
    print(getNode(a.head, pos))