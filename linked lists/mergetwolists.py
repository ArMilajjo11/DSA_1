class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def printList(self):
        if self.head is None:
            print("List is empty ")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

def merge(headA, headB):
    dummynode = Node(0)
    temp = dummynode
    while True:
        if headA is None:
            temp.next = headB
            break
        elif headB is None:
            temp.next = headA
            break

        if headA.data >= headB.data:
            temp.next = headB
            headB = headB.next
        else:
            temp.next = headA
            headA = headA.next
        temp = temp.next
    return dummynode.next

t = int(input("Enter test cases: "))
for i in range(t):
    a = LL()
    l1 = int(input("Enter length of list 1: "))
    for j in range(l1):
        num1 = int(input("Enter num: "))
        a.push(num1)
    b = LL()
    l2 = int(input("Enter length of list 2: "))
    for j in range(l2):
        num2 = int(input("Enter num: "))
        b.push(num2)
    a.head = merge(a.head, b.head)
    a.printList()


