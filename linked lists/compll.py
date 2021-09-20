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

def compare_lists(head1, head2):
    if n1 != n2:
        return 0
    else:
        while (head1 is not None) and (head2 is not None):
            if head1.data != head2.data:
                return 0
            else:
                head1 = head1.next
                head2 = head2.next
        return 1

test = int(input("Enter tests: "))
for i in range(test):
    a = Linked_list()
    n1 = int(input("Enter length1: "))
    for j in range(n1):
        num1 = int(input("Enter elements: "))
        a.push(num1)
    b = Linked_list()
    n2 = int(input("Enter length2: "))
    for k in range(n2):
        num2 = int(input("Enter elements: "))
        b.push(num2)
    print(compare_lists(a.head, b.head))







