import copy
import math
import queue
import random
from enum import Enum

class Color(Enum):
    WHITE = 0
    GRAY = 127
    BLACK = 255

class Graph:




    def __init__(self):
        self.Nodes = []
        self.Edges = []
        self.ts = []
        self.Components = []
        self.minTree = []


    class Node:

        def __init__(self, color=None, d=None, p=None, val=None, f=None):
            self.adj = []
            self.color = color
            self.d = d
            self.p = p
            self.val = val
            self.f = f          # DFS

        def __lt__(self, other):
            if self.d < other.d:
                return True
            return False


    class Edge:

        def __init__(self, src=None, dst=None, w=None):
            self.src = src
            self.dst = dst
            self.w = w

    def insertNode(self, n):
        self.Nodes.append(n)
        return self

    def insertNodes(self, n):
        for i in n:
            self.Nodes.append(i)


    def connectNodes(self, u, v, w = 1):
        for e in self.Edges:
            if e.src == u and e.dst == v:
                e.w = w
        self.Edges.append(Graph.Edge(u, v, w))
        u.adj.append(v)

    def connectUndirected(self, u, v, w = 1):
        for e in self.Edges:
            if e.src == u and e.dst == v:
                e.w = w
            elif e.src == v and e.dst == u:
                e.w = w
        self.Edges.append(Graph.Edge(u, v, w))
        self.Edges.append(Graph.Edge(v, u, w))
        u.adj.append(v)
        v.adj.append(u)


    def printNeighbors(self, n):
        for i in self.Nodes:
            if i.val == n:
                for j in i.adj:
                    print(j.val)

    def printConnections(self, n):
        for i in self.Edges:
            if i.src == n or i.dst == n:
                print(i)

    def BFS(self, s):
        for i in self.Nodes:
            i.color = Color.WHITE
            i.d = math.inf
            i.p = None
        s.color = Color.GRAY
        s.d = 0
        s.p = None
        Q = queue.Queue()
        Q.put(s)
        while Q.empty() == False:
            u = Q.get()
            for v in u.adj:
                if v.color == Color.WHITE:
                    v.color = Color.GRAY
                    v.d = u.d + 1
                    v.p = u
                    Q.put(v)
            u.color = Color.BLACK

    def printPath(self, s, v):
        if v == s:
            print(s.val)
        elif v.p == None:
            print("No path from ", s.val, " to ", v.val, " exists.")
        else:
            self.printPath(s, v.p)
            print(v.val)


    def DFS(self):
        for u in self.Nodes:
            u.color = Color.WHITE
            u.p = None
        global time
        time = 0
        for u in self.Nodes:
            if u.color == Color.WHITE:
                self.DFS_Visit(u)

    def DFS_Visit(self, u):
        global time
        time += 1
        global i
        u.d = time
        u.color = Color.GRAY
        for v in u.adj:
            if v.color == Color.WHITE:
                v.p = u
                self.DFS_Visit(v)
        u.color = Color.BLACK
        time += 1
        u.f = time
        self.ts.append(u)

    def topologicalSort(self):
        self.ts = []
        self.DFS()
        ts = self.ts
        self.ts = []
        return ts

    def initializeSingleSource(self, s):
        for v in self.Nodes:
            v.d = math.inf
            v.p = None
        s.d = 0

    def relax(self, u, v, w):
        if v.d > u.d + w:
            v.d = u.d + w
            v.p = u

    def Dijkstra(self, s):
        self.initializeSingleSource(s)
        S = []
        Q = queue.PriorityQueue()
        for v in self.Nodes:
            Q.put(v)
        while Q.empty() == False:
            u = Q.get()
            S.append(u)
            for v in u.adj:
                w = self.findWeight(u, v)
                self.relax(u, v, w)

    def BellmanFord(self, s):
        self.initializeSingleSource(s)
        w = 0
        for u in self.Nodes:
            for v in u.adj:
                w = self.findWeight(u, v)
                self.relax(u, v, w)
        for e in self.Edges:
            if e.dst.d > e.src.d + self.findWeight(e.src, e.dst):
                print("Negative cycle detected!")
                return False
        return True

    def findWeight(self, u, v):
        for e in self.Edges:
            if e.src == u and e.dst == v:
                return e.w
        return None

    def ShortestPath(self, u, v):
        self.BellmanFord(u)
        path = []
        length = v.d
        while u != v:
            path.append(v.val)
            v = v.p
        path.append(u.val)
        return (path[::-1], length)

    def UpdateEdge(self, u, v, w):
        for e in self.Edges:
            if e.src == u and e.dst == v:
                e.w = w
                return
        self.connectNodes(u, v, w)

    def GetInDegrees(self):
        inDgr = []
        for v in self.Nodes:
            inDgr.append(0)
        for i in range(len(self.Nodes)):
            for e in self.Edges:
                if self.Nodes[i] == e.dst:
                    inDgr[i] += 1
        return inDgr

    def GetOutDegrees(self):
        outDgr = []
        for v in self.Nodes:
            outDgr.append(len(v.adj))
        return outDgr

    def ApplyStronglyConnectedComponents(self):
        self.DFS()
        Gt = self.TransposeGraph()
        Gt.ApplyDFSInOrder()
        Gt.PrintStronglyConnectedComponents()

    def PrintStronglyConnectedComponents(self):
        for c in self.Components:
            print(c)


    def TransposeGraph(self):
        Gt = copy.deepcopy(self)
        for e in Gt.Edges:
            e.src, e.dst = e.dst, e.src
        return Gt

    def ApplyDFSInOrder(self):
        self.SortDescending()
        self.modDFS()

    def modDFS(self):
        for u in self.Nodes:
            u.color = Color.WHITE
            u.p = None
        global time
        time = 0
        global it
        it = 0
        for u in self.Nodes:
            if u.color == Color.WHITE:
                self.Components.append([])
                self.modDFS_Visit(u)
                it += 1

    def modDFS_Visit(self, u):
        global time
        time += 1
        global it
        self.Components[it].append(u.val)
        u.d = time
        u.color = Color.GRAY
        for v in u.adj:
            if v.color == Color.WHITE:
                v.p = u
                self.modDFS_Visit(v)
        u.color = Color.BLACK
        time += 1
        u.f = time
        self.ts.append(u)


    def SortDescending(self):
        for j in range(1, len(self.Nodes)):
            key = self.Nodes[j]
            i = j - 1
            while i >= 0 and key.f < self.Nodes[i].f:
                self.Nodes[i+1] = self.Nodes[i]
                i -= 1
            self.Nodes[i+1] = key


    def Prim(self, r):
        for u in self.Nodes:
            u.d = math.inf
            u.p = None
        r.d = 0
        Q = queue.PriorityQueue()
        for n in self.Nodes:
            Q.put(n)
        ejected = []
        while Q.empty() == False:
            u = Q.get()
            ejected.append(u.val)
            for v in u.adj:
                if self.findWeight(u, v) < v.d and ((v.val in ejected) == False):
                    v.p = u
                    v.d = self.findWeight(u, v)




def generateRandomGraph(n, e):
    G = Graph()
    for i in range(n):
        node_exists = False
        v = Graph.Node(val = chr(random.randint(98, 122)))
        for u in G.Nodes:
            if u.val == v.val:
                node_exists = True
        if node_exists == False:
            G.insertNode(v)
    for i in range(random.randint(e // 2, e)):
        edge_exists = False
        u = G.Nodes[random.randint(0, len(G.Nodes)-1)]
        v = G.Nodes[random.randint(0, len(G.Nodes)-1)]
        w = random.randint(0, 100)
        for e in G.Edges:
            if e.src == u and e.dst == v:
                edge_exists = True
                break
        if edge_exists == False:
            G.connectNodes(u, v, w)
    return G



