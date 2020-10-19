
import math
from vertex_example import *

def BFS(G, s):
    for i in G:
        i.d = math.inf
        i.c = VertexColor.WHITE
    s.d = 0
    s.c = VertexColor.GRAY
    Q = []
    Q.append(s)
    while len(Q) != 0:
        u = Q.pop()
        for i in u.a:
            if i.c == VertexColor.WHITE:
                i.c = VertexColor.GRAY
                i.d = u.d + 1
                i.pi = u
                Q.append(i)
        u.c = VertexColor.BLACK

def PrintPath(G, s, v):
    if v == s:
        print(s.d)
    elif v.pi == None:
        print("No path from vertexes exists.")
    else:
        PrintPath(G, s, v.pi)
        print(v.d)


if __name__ == "__main__":

    # Zadatak 2

    r = Vertex([])
    s = Vertex([])
    t = Vertex([])
    u = Vertex([])
    v = Vertex([])
    x = Vertex([])
    y = Vertex([])
    w = Vertex([])

    r.a += [v, s]
    s.a += [r, w]
    t.a += [w, x, u]
    u.a += [t, x, y]
    v.a += [r]
    x.a += [w, t, u, y]
    y.a += [x, u]
    w.a += [s, t, x]

    graph = [s, r, t, u, v, x, y, w]

    BFS(graph[1:], graph[0])

    PrintPath(graph, s, v)


