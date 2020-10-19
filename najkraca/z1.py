from graph import *
import math
import copy


def InitializeSingleSource(G, s):
    for v in G:
        v.d1 = math.inf
        v.p = None
    s.d1 = 0


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

    s.d2 = "s"
    t.d2 = "t"
    x.d2 = "x"
    y.d2 = "y"
    z.d2 = "z"

    G = [s, t, x, y, z]

    InitializeSingleSource(G, s)


