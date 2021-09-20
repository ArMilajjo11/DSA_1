class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self, data):
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

def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

a = BinaryTree()
l = int(input("Enter length: "))
for i in range(l):
    num = int(input("Enter num: "))
    a.create(num)
preorder(a.root)

