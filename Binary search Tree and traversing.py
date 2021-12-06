class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    # Inorder traversal
    # Left -> Root -> Right
    def inordertraversal(self):
        elements = []
        if self.left:
            elements += self.left.inordertraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inordertraversal()
        return elements

    #preordertraversal
    # Root -> Left ->Right
    def preordertraversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.preordertraversal()

        if self.right:
            elements += self.right.preordertraversal()
        return elements

    # Postorder traversal
    # Left ->Right -> Root
    def postordertraversal(self):
        elements=[]

        if self.left:
            elements += self.left.postordertraversal()

        if self.right:
            elements += self.right.postordertraversal()

        elements.append(self.data)
        return elements


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print('Traversing BST in in-order-traversal: {}'.format(root.inordertraversal()))
print('Traversing BST in pre-order-traversal: {}'.format(root.preordertraversal()))
print('Traversing BST in post-order-traversal: {}'.format(root.postordertraversal()))

