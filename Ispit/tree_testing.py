import bst
import random

if __name__ == "__main__":

    T = bst.Tree()
    for i in range(10):
        T.treeInsert(bst.Node(d = bst.Data(random.randint(0, 100))))
    T.treeInsert(bst.Node(d = bst.Data(10)))

    print("Root: ", T.root.key())

    T.inorderTreeWalk(T.root)
    print("---------------")
    n = T.treeSearch(T.root, 10)
    if n != None:
        T.treeDelete(T.treeMinimum(n))
    print("---------------")
    T.inorderTreeWalk(T.root)


    print("Root: ", T.root.key())

    print("Min ", T.treeMinimum(T.root).key())

    print("Max: ", T.treeMaximum(T.root).key())

    print("root successor: ", T.treeSuccessor(T.root).key())