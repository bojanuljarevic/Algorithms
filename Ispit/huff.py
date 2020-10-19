import queue

class Node:

    def __init__(self, p = None, l = None, r = None, f = None, ch = None):
        self.p = p
        self.l = l
        self.r = r
        self.f = f
        self.ch = ch

    def freq(self):
        return self.f

    def key(self):
        return self.ch

class Tree:

    def __init__(self, root):
        self.root = None

    def treeSearch(self, x , k):
        if x == None or k == x.key():
            return x
        if k < x.key():
            return self.treeSearch(x.l, k)
        else:
            return self.treeSearch(x.r, k)

def getHistogram(input):
    hist = {}
    for i in input:
        hist[i] = 0
    for i in input:
        hist[i] += 1
    return hist

def Huffman(c):

    Q = queue.PriorityQueue()
    for i in c:
        Q.put((c[i], i))

    for i in range(len(c)-1):
        z = Node()
        x = Q.get()
        y = Q.get()
        z.l = Node(p = z, f = x[0], ch = x[1])
        z.r = Node(p = z, f = y[0], ch = y[1])
        z.f = z.l.f + z.r.f
        z.ch = z.l.ch + z.r.ch
        Q.put((z.f, z.ch))
    return z


if __name__ == "__main__":

    input1 = ['a', 'b']
    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']

    h = getHistogram(input5)

    root = Huffman(h)

    T = Tree(root)

    leaf = T.treeSearch(root)
    print(leaf.f)


    # URADITI S KLASAMA KAKO TREBA

