
import math

class Graph:

    class Node:

        def __init__(self, p = None, d = None, val = None):
            self.p = p
            self.d = d
            self.val = val
            self.adj = []

    class Edge:

        def __init__(self, src = None, dst = None, w = 1):
            self.src = src
            self.dst = dst
            self.w= w


    def __init__(self):
        self.Nodes = []
        self.Edges = []

    def insertNode(self, n):
        self.Nodes.append(n)
        return self

    # zadatak 2

    def GetInDegrees(self):
        inDgr = [0] * len(self.Nodes)
        for i in range(len(self.Nodes)):
            for e in self.Edges:
                if e.dst == self.Nodes[i]:
                    inDgr[i] += 1
        return inDgr

    def GetOutDegrees(self):
        outDgr = []
        for n in self.Nodes:
            outDgr.append(len(n.adj))
        return outDgr

    # zadatak 3

    def findWeight(self, u, v):
        for e in self.Edges:
            if e.src == u and e.dst == v:
                return e.w
        return None

    def InitializeSingleSource(self, s):
        for n in self.Nodes:
            n.d = math.inf
            n.p = None
        s.d = 0

    def Relax(self, u, v):
        w = self.findWeight(u, v)
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def BellmanFord(self, u):
        self.InitializeSingleSource(u)
        for n in self.Nodes:
            for e in self.Edges:
                self.Relax(e.src, e.dst)
        for e in self.Edges:
            if e.dst.d > e.src.d + self.findWeight(e.src, e.dst):
                return False
        return True

    def ShortestPath(self, u, v):
        self.BellmanFord(u)
        path = []
        d = v.d
        while v != u:
            if v.p == None:
                return ([], math.inf)
            path.append(v.val)
            v = v.p
        path.append(u.val)
        return (path[::-1], d)

    # zadatak 4
    def updateEdge(self, u, v, w):
        for e in self.Edges:
            if e.src == u and e.dst == v:
                e.w = w
        self.Edges.append(Graph.Edge(u, v, w))
        u.adj.append(v)

# zadatak 1
def makeGraph():

    a = Graph.Node(val='a')
    b = Graph.Node(val='b')
    c = Graph.Node(val='c')
    d = Graph.Node(val='d')
    e = Graph.Node(val='e')
    f = Graph.Node(val='f')
    g = Graph.Node(val='g')
    h = Graph.Node(val='h')
    G = Graph()
    G.insertNode(a).insertNode(b).insertNode(c).insertNode(d)
    G.insertNode(e).insertNode(f).insertNode(g).insertNode(h)
    G.updateEdge(a, b, 5)
    G.updateEdge(a, d, 8)
    G.updateEdge(b, d, 9)
    G.updateEdge(d, c, 1)
    G.updateEdge(d, e, 10)
    G.updateEdge(d, f, 13)
    G.updateEdge(e, g, 7)
    G.updateEdge(f, g, 20)
    G.updateEdge(h, c, 16)
    G.updateEdge(h, e, 2)
    G.updateEdge(h, g, 24)
    return G


if __name__ == "__main__":

    # zadatak 1
    G = makeGraph()

    #zadatak 2
    print(G.GetInDegrees())
    print(G.GetOutDegrees())

    # zadatak 3
    a = G.Nodes[0]
    g = G.Nodes[6]
    c = G.Nodes[2]
    print("Putanja od A do G: ", G.ShortestPath(a, g))
    # putanja koja ne postoji:
    print("Putanja od C do G: ", G.ShortestPath(c, g))

    # zadatak 4, 5
    d = G.Nodes[3]
    G.updateEdge(d, g, -4)
    print("Putanja od A do G nakon dodavanja (D,G): ", G.ShortestPath(a, g))

    # zadatak 6, na primjeru cvorove H i G, i ivice (H, G)
    h = G.Nodes[7]
    print("Putanja od H do G: ", G.ShortestPath(h, g))
    G.updateEdge(h, g, 8)
    print("Putanja od H do G nakon azuriranja (H, G): ", G.ShortestPath(h, g))


