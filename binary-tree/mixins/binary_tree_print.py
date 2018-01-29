class BinaryTreePrintMixin():
    """Traverses and prints a BinaryTree as a Mixin"""

    def printTree(self):
        tree = self
        self.printTreeNode(tree)
        self.printTreeBranches(tree)

    def printTreeNode(self, tree):
        if tree != None:
            print("%s is the root node" % tree.getNodeValue())

    def printTreeBranches(self, tree):
        if tree != None:
            if tree.getLeftChild():
                node = tree.getNodeValue()
                child = tree.getLeftChild().getNodeValue()
                print("%ss left branch child is %s" % (node, child))
                self.printTreeBranches(tree.getLeftChild())

            if tree.getRightChild():
                node = tree.getNodeValue()
                child = tree.getRightChild().getNodeValue()
                print("%ss right branch child is %s" % (node, child))
                self.printTreeBranches(tree.getRightChild())
