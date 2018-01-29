from classes.binary_tree import BinaryTree
from mixins.binary_tree_print import BinaryTreePrintMixin
from mixins.binary_tree_reverse import BinaryTreeReverseMixin

class EnhancedBinaryTree(BinaryTree, BinaryTreePrintMixin, BinaryTreeReverseMixin):
    pass
