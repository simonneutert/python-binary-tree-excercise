# Binary Trees it is

``` python
# main.py
def buildTestTree():
    myTree = EnhancedBinaryTree("Rick")
    myTree.insertLeft("Morty")
    myTree.insertRight("Noobnoob")
    myTree.insertRight("Antman")
    return myTree


print("\nRunning example:\n")

sample_tree = buildTestTree()
print("Printing tree:\r")
sample_tree.printTree()

print("\r")

rev_tree = sample_tree.reverse_tree()
print("Printing reversed tree:\r")
rev_tree.printTree()
```

---
__Output__
``` text
print tree:

Printing tree:
Rick is the root node
Ricks left branch child is Morty
Ricks right branch child is Antman
Antmans right branch child is Noobnoob

Printing reversed tree:
Rick is the root node
Ricks left branch child is Antman
Antmans left branch child is Noobnoob
Ricks right branch child is Morty
```
---
