class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.temp = None

    def insatpos(self, data, pos):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            index = pos - 1
            temp = self.head
            count = 0
            while temp.next is not None:
                if count == index:
                    break
                else:
                    prev = temp
                    temp = temp.next
                    count = count + 1
            posnode = node
            prev.next = posnode
            posnode.next = temp

    def insertattail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.temp.next = node
        self.temp = node

    def prinlist(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next


a = LL()
n = int(input("Enter length "))
for i in range(n):
    num = int(input("Enter num "))
    a.insertattail(num)

pos = int(input("Enter position "))
data = int(input("Enter data "))
a.insatpos(data, pos)
print("Hence list: ")
a.prinlist()
