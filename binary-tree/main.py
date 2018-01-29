from classes.binary_tree_enhanced import EnhancedBinaryTree


def buildTestTree():
    myTree = EnhancedBinaryTree("Rick")
    myTree.insertLeft("Morty")
    myTree.insertRight("Noobnoob")
    myTree.insertRight("Antman")
    return myTree


if __name__ == '__main__':
    print("\nRunning example:\n")

    sample_tree = buildTestTree()
    print("Printing tree:\r")
    sample_tree.printTree()

    print("\r")

    rev_tree = sample_tree.reverse_tree()
    print("Printing reversed tree:\r")
    rev_tree.printTree()
