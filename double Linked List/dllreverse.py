class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp

    def reverse(self):
        if self.head is None:
            print("List is empty")
        else:
            pre = None
            current = self.head
            following = current.next
            while current is not None:
                current.prev = current.next
                current.next = pre
                pre = current
                current = following
                if following is not None:
                    following = following.next
            self.head = pre
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

    def printList(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

t = int(input("Test cases: "))
for i in range(t):
    l = int(input("Enter length: "))
    a = DLL()
    for j in range(l):
        num = int(input("Enter num: "))
        a.append(num)
    a.printList()
    print()
    a.reverse()
