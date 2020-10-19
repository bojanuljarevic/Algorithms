
# Zadatak 1 : ručno formiranje binarnog stabla pretrage

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        """
        Node constructor
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

    def addLeft(self, data):
        child = Node(self, None, None, data)
        self.left = child
        return child

    def addRight(self, data):
        child = Node(self, None, None, data)
        self.right = child
        return child

    def printNode(self):
        print(self.data.a1, self.data.a2)
        '''if(self.left != None):
            print("Has left child")
        else:
            print("Does not have left child")
        if (self.right != None):
            print("Has right child")
        else:
            print("Does not have right child")'''


class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2




if __name__ == "__main__":

    root_data = Data(48, chr(48))
    left_data = Data(49, chr(49))
    right_data = Data(50, chr(50))
    root = Node(None, None, None, root_data)
    left_child = root.addLeft(left_data)
    right_child = root.addRight(right_data)

    root.printNode()

    left_child.printNode()

    right_child.printNode()

    left_child.parent.printNode()






