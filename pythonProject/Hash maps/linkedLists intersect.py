class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
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

    def print(self):
        if self.head is None:
            print("empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

a = LL()
b = LL()
lla = list(map(int, input("Enter first list: ").split()))
llb = list(map(int, input("Enter second list: ").split()))
for i in lla:
    a.append(i)
for j in llb:
    b.append(j)

a.print()
print()
b.print()