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

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next


# def delduplicate(head):
#     temp = head
#     dummynode = Node(0)
#     prev = dummynode
#     dummytwo = Node(0)
#     newhead = dummytwo
#     while temp.next is not None:
#         if temp.data == prev.data:
#             continue
#         else:
#             prev = temp
#             newhead.next = prev
#             temp = temp.next
#     return newhead

def delduplicate(head):
    temp = head
    while temp.next is not None:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = None
            temp.next = new
        else:
            temp = temp.next
    return head


t = int(input("Enter test cases: "))
for i in range(t):
    l = int(input("Enter length: "))
    a = LL()
    for j in range(l):
        n = int(input("Enter " + str(j + 1) + " number: "))
        a.push(n)
    a.print_list()
    print()
    a.head = delduplicate(a.head)
    a.print_list()
