class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            temp = self.root
            while True:
                if data > temp.data:
                    if temp.right is None:
                        temp.right = Node(data)
                        break
                    else:
                        temp = temp.right
                elif data < temp.data:
                    if temp.left is None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
                else:
                    break

def postorder(root):
    if root.right is None:
        return
    else:
        print(root.right.data)
        postorder(root.right.right)
        postorder()
