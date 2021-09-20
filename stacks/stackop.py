items = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        items.append(max(nums[1], items[-1]))
    elif nums[0] == 2:
        items.pop()
    else:
        print(items[-1])

# linked list approach
'''class Node:
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
            print("Stack is underflow")
        else:
            n = self.top
            self.top = self.top.next
            n.next = None

    def max(self):
        n = self.top
        maxvalue = self.top.data
        while n is not None:
            if n.data > maxvalue:
                maxvalue = n.data
            else:
                n = n.next
        return maxvalue

n = int(input())
a = Stack()
for i in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        a.push(q[1])
    elif q[0] == 2:
        a.pop()
    elif q[0] == 3:
        print(a.max())'''

# deque approach
"""from collections import deque
n = int(input())
stack = deque([])
for i in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        stack.appendleft(q[1])
    elif q[0] == 2:
        stack.popleft()
    elif q[0] == 3:
        mx = max(stack)
        print(mx)"""
