from graph import *
import math
import copy


def InitializeSingleSource(G, s):
    for v in G:
        v.d1 = math.inf
        v.p = None
    s.d1 = 0

def Relax(u, v, w):
    if v.d1 > u.d1 + w:
        v.d1 = u.d1 + w
        v.p = u

def Dijkstra(G, s):
    InitializeSingleSource(G, s)
    S = []
    Q = copy.deepcopy(G)
    while len(Q) > 0:
        u = ExtractMin(Q)
        S.append(u)
        for edge in u.e:
            Relax(u, edge.dst, edge.w)
    return S

def ExtractMin(Q):
    v = Q[0]
    for i in Q:
        if i.d1 < v.d1:
            v = i
    Q.remove(v)
    return v


if __name__ == "__main__":

    s = Vertex(VertexColor.GRAY)
    t = Vertex(VertexColor.WHITE)
    x = Vertex(VertexColor.WHITE)
    y = Vertex(VertexColor.WHITE)
    z = Vertex(VertexColor.WHITE)

    s.e.append(Edge(s, t, 10))
    s.e.append(Edge(s, y, 5))

    t.e.append(Edge(t, x, 1))
    t.e.append(Edge(t, y, 2))

    x.e.append(Edge(x, z, 4))

    y.e.append(Edge(y, t, 3))
    y.e.append(Edge(y, x, 9))
    y.e.append(Edge(y, z, 2))

    z.e.append(Edge(z, s, 7))
    z.e.append(Edge(z, x, 6))

    G = [s, t, x, y, z]

    S = Dijkstra(G, s)

    for v in S:
        print(v.d1)



