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
        if not self.head:
            self.head = node
        else:
            self.temp.next = node
        self.temp = node

    def print_list(self):
        if not self.head:
            print("list empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

def reverse_list(head):
    if not head:
        print("list empty")
    else:
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
    m = head
    while m is not None:
        print(m.data)
        m = m.next

test = int(input("Enter number of test case: "))
for i in range(test):
    l = int(input("Enter length of list: "))
    a = Linked_list()
    for j in range(l):
        num = int(input("Enter element: "))
        a.push(num)
    reverse_list(a.head)








