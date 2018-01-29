class BinaryTree():
    def __init__(self, root_value):
        self.left_branch = None
        self.right_branch = None
        self.root_value = root_value

    def setNodeValue(self, value):
        self.root_value = value

    def getNodeValue(self):
        return self.root_value

    def getRightChild(self):
        return self.right_branch

    def insertRight(self, newNode):
        if self.right_branch == None:
            self.right_branch = BinaryTree(newNode)
        else:
            sub_branch = BinaryTree(newNode)
            sub_branch.right_branch = self.right_branch
            self.right_branch = sub_branch

    def getLeftChild(self):
        return self.left_branch

    def insertLeft(self, newNode):
        if self.left_branch == None:
            self.left_branch = BinaryTree(newNode)
        else:
            sub_branch = BinaryTree(newNode)
            sub_branch.left_branch = self.left_branch
            self.left_branch = sub_branch
