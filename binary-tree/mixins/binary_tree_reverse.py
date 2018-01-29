from classes.binary_tree_helper import HelperBinaryTree

class BinaryTreeReverseMixin():
    """Reverse a BinaryTree's Structure as a Mixin"""

    def reverse_tree(self):
        reverse_tree = HelperBinaryTree(self.getNodeValue())
        reverse_tree.left_branch = None
        reverse_tree.right_branch = None
        self.reverseTreeBranches(self, reverse_tree)
        return reverse_tree

    def reverseTreeBranches(self, tree, reverse_tree):
        if tree != None:
            if tree.getLeftChild():
                node = tree.getNodeValue()
                child = tree.getLeftChild().getNodeValue()
                if reverse_tree.right_branch == None:
                    reverse_tree.right_branch = HelperBinaryTree(child)
                else:
                    reverse_tree.right_branch.right_branch = HelperBinaryTree(child)
                self.reverseTreeBranches(tree.getLeftChild(), reverse_tree.getLeftChild())

            if tree.getRightChild():
                node = tree.getNodeValue()
                child = tree.getRightChild().getNodeValue()
                if reverse_tree.left_branch == None:
                    reverse_tree.left_branch = HelperBinaryTree(child)
                else:
                    reverse_tree.left_branch.left_branch = HelperBinaryTree(child)
                self.reverseTreeBranches(tree.getRightChild(), reverse_tree.getLeftChild())
