
from vertex_example import *

def DFS(G):
    for u in G:
        u.c = VertexColor.WHITE
        u.pi = None
    time = 0
    for u in G:
        if u.c == VertexColor.WHITE:
            DFSVisit(G, u, time)


def DFSVisit(G, u, time):
    time += 1
    u.d = time
    u.c = VertexColor.GRAY
    for v in u.a:
        if v.c == VertexColor.WHITE:
            v.pi = u
            DFSVisit(G, v, time)
    u.c = VertexColor.BLACK
    time += 1
    u.f = time


def PrintPath(G, s, v):
    if v == s:
        print(s.d)
    elif v.pi == None:
        print("No path from vertexes exists.")
    else:
        PrintPath(G, s, v.pi)
        print(v.f)


if __name__ == "__main__":


    # ZADATAK 3

    u = Vertex([])
    v = Vertex([])
    w = Vertex([])
    x = Vertex([])
    y = Vertex([])
    z = Vertex([])

    u.a += [v, x]
    v.a += [y]
    w.a += [y, z]
    x.a += [v]
    y.a += [x]
    z.a += [z]

    G = [u, v, w, x, y, z]

    DFS(G)

    #PrintPath(G, u, v)
