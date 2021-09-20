class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.temp = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            print("Stack underflow")
        else:
            n = self.top
            self.top = self.top.next
            n.next = None
            return n.data

    def peek(self):
        if self.top is None:
            print("stack empty")
        else:
            return self.top.data

    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            n = self.top
            while n is not None:
                print(n.data)
                n = n.next


a = Stack()
n = int(input("Enter length: "))
for i in range(n):
    num = int(input("Enter num: "))
    a.push(num)
a.display()
print("popped element is " + str(a.pop()))
a.display()
print()
print(a.peek())


