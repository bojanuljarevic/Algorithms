
class Node:

    def __init__(self, p = None, l = None, r = None, d = None):
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

    def printNode(self):
        print(self.data.key)

class Data:
    '''Modelovao sam podatke stabla kao ključ + vrijednost radi opšteg slučaja
    parametar vrijednost je zanemarljiv u zadatku te sam svaku instancu u testiranju postavio na None'''
    def __init__(self, val1, val2):
        self.key = val1
        self.value = val2


# Zadatak 2: inorder prolazak kroz stablo

def inOrderTreeWalk(x):
    if x != None:
        inOrderTreeWalk(x.left)
        x.printNode()
        inOrderTreeWalk(x.right)

# Zadatak 3: Rekurzivna i iterativna pretraga stabla

def TreeSearch(x, k):
    if x == None or x.data.key == k:
        return x
    if x.data.key < k:
        return TreeSearch(x.right, k)
    return TreeSearch(x.left, k)

def IterativeTreeSearch(x, k):
    while x != None and x.data.key != k:
        if k < x.data.key:
            x = x.left
        else:
            x = x.right
    return x

# Zadatak 4: Minimum, maksimum i nasljednik

def treeMinimum(x):
    while x.left != None:
        x = x.left
    return x

def treeMaximum(x):
    while x.right != None:
        x = x.right
    return x


def treeSuccessor(x):
    if x.right != None:
        return treeMinimum(x.right)
    y = x.parent
    while y != None and x == y.right:
        x = y
        y = y.parent
    return y

# Zadatak 5: Umetanje, brisanje i subrutina Transplant

def treeInsert(x,z):
    y = None
    while x != None:
        y = x
        if z.data.key < x.data.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        x = z
    elif z.data.key < y.data.key:
        y.left = z
        z.parent = y
    else:
        y.right = z
        z.parent = y


def treeDelete(x,z):
    if z.left == None:
        transplant(x,z, z.right)
    elif z.right == None:
        transplant(x,z, z.left)
    else:
        y = treeMinimum(z.right)
        if y.parent != z:
            transplant(x, z, y)
            y.right = z.right
            y.right.parent = y
        transplant(x,z, y)
        y.left = z.left
        y.left.parent = y

def transplant(x,u,v):
    if u.parent == None:
        x = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v != None:
        v.parent = u.parent



# Ručno testiranje:
'''
if __name__ == "__main__":

    root = Node(None, None, None, Data(15, None))
    n1 = Node(None, None, None, Data(12, None))
    n2 = Node(None, None, None, Data(100, None))
    n3 = Node(None, None, None, Data(5, None))
    n4 = Node(None, None, None, Data(65, None))
    n5 = Node(None, None, None, Data(125, None))

    treeInsert(None, root)
    treeInsert(root, n1)
    treeInsert(root, n2)
    treeInsert(root, n3)
    treeInsert(root, n4)
    treeInsert(root, n5)

    print("Prvobitno:")
    inOrderTreeWalk(root)

    treeDelete(root, n4)

    print("Nakon brisanja:")
    inOrderTreeWalk(root)
'''
# Generisano testiranje:

import random

def generateRandomList(min, max, n):
    L =[]
    for i in range(n):
        L.append(random.randint(min, max))
    return L

def modifiedInorderTreeWalk(x, list):
    if x != None:
        modifiedInorderTreeWalk(x.left, list)
        list.append(x.data.key)
        modifiedInorderTreeWalk(x.right, list)

if __name__ == "__main__":

    n = 32
    L1 = generateRandomList(0, 100, n)

    root = Node(None, None, None, Data(L1[0], None))
    for i in range(1, n):
        treeInsert(root, Node(None, None, None, Data(L1[i], None)))
        # prije unosenja u stablo čvor je nezavisan entitet pa su mu polja
        # parent, left i right postavljeni na None
        # Ovo se modifikuje u odgovarajućim funkcijama stabla

    L2 = []
    modifiedInorderTreeWalk(root, L2)

    L1.sort()
    if L1.__eq__(L2):
        print("Korektno")

    print(L2)
