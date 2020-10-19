
# Tree node
class Node:

    def __init__(self, p = None, l = None, r = None, d = None):
        self.p = p
        self.l = l
        self.r = r
        self.d = d

    def key(self):
        return self.d.val


# Satelite data
class Data:

    def __init__(self, val):
        self.val = val

    def printData(self):
        print(self.val)



class Tree:

    def __init__(self):
        self.root = None

    def inorderTreeWalk(self, x):
        if x != None:
            self.inorderTreeWalk(x.l)
            x.d.printData()
            self.inorderTreeWalk(x.r)

    def treeSearch(self, x , k):
        if x == None or k == x.key():
            return x
        if k < x.key():
            return self.treeSearch(x.l, k)
        else:
            return self.treeSearch(x.r, k)

    def treeMinimum(self, x):
        while x.l != None:
            x = x.l
        return x

    def treeMaximum(self, x):
        while x.r != None:
            x = x.r
        return x

    def treeSuccessor(self, x):
        if x.r != None:
            return self.treeMinimum(x.r)
        y = x.p
        while y != None and x == y.r:
            x = y
            y = y.p
        return y

    def treeInsert(self, z):
        if self.root == None:
            self.root = z
            return
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key() < x.key():
                x = x.l
            else:
                x = x.r
        z.p = y
        if y == None:
            self.root = z
        elif z.key() < y.key():
            y.l = z
        else:
            y.r = z


    def treeDelete(self, z):
        if z.l == None:
            self.transpant(z, z.r)
        elif z.r == None:
            self.transpant(z, z.l)
        else:
            y = self.treeMinimum(z.r)
            if y.p != z:
                self.transpant(y, y.r)
                y.r = z.r
                y.r.p = y
            self.transpant(z, y)
            y.l =  z.l
            y.l.p = y


    def transpant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.l:
            u.p.l = v
        else:
            u.p.r = v
        if v != None:
            v.p = u.p