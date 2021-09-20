# Detect loop in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def loop(self,pos):
        if pos < 0:
            return
        else:
            temp = self.head
            count = 0
            while temp.next is not None:
                if count == pos:
                    n = temp
                temp = temp.next
                count += 1
            temp.next = n

    def printList(self):
        if self.head is None:
            print('List is empty')
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

def detectLoop(head):
    if head is None:
        return False
    elif head.next is None:
        return False
    else:
        hare = head
        tortoise = head
        while hare is not None and hare.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                return True
        return False

a = linkedList()
l = int(input("Enter length: "))
for i in range(l):
    num = int(input("enter number: "))
    a.append(num)
a.printList()
pos = int(input("Enter position "))
a.loop(pos)
print(detectLoop(a.head))