class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def push(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
                elif data > temp.data:
                    if temp.right is None:
                        temp.right = Node(data)
                        break
                    else:
                        temp = temp.right
                else:
                    break


def MaxHeight(root):
    if root is None:
        return -1
    else:
        lh = MaxHeight(root.left)
        rh = MaxHeight(root.right)

        if lh > rh:
            return lh+1
        else:
            return rh+1

def preorder(root):
    if root is None:
        return 0
    print(root.data)
    preorder(root.left)
    preorder(root.right)

n = int(input("Enter the number of nodes: "))
nodes = list(map(int, input("Enter nodes: ").split()))
a = Tree()
for i in range(n):
    a.push(nodes[i])

print(preorder(a.root))
print(MaxHeight(a.root))