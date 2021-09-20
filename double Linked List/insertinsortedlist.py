class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class doubleLL:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)
        node.next = None
        if self.head is None:
            node.prev = None
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp

    def sortedpush(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return self.head
        elif self.head.data > node.data:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return self.head
        else:
            temp = self.head
            following = temp.next
            while temp.next is not None:
                if following.data > node.data:
                    temp.next = node
                    node.prev = temp
                    node.next = following
                    following.prev = node
                    return self.head
                else:
                    temp = temp.next
                    following = temp.next
            following.next = node
            node.prev = following
            return self.head

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next


def pl(head):
    if head is None:
        print("list is empty")
    else:
        n = head
        while n is not None:
            print(n.data)
            n = n.next


test = int(input("Enter no. of test cases: "))
for i in range(test):
    a = doubleLL()
    length = int(input("Enter length: "))
    for j in range(length):
        num = int(input("Enter number: "))
        head = a.sortedpush(num)
    pl(a.head)


