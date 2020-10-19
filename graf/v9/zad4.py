
from vertex_example import *

def DFS(G, l):
    for u in G:
        u.c = VertexColor.WHITE
        u.pi = None
    global time
    time = 0
    for u in G:
        if u.c == VertexColor.WHITE:
            DFSVisit(G, u, l)



def DFSVisit(G, u, l):
    global time
    u.d = time
    u.c = VertexColor.GRAY

    for v in u.a:
        if v.c == VertexColor.WHITE:
            v.pi = u
            DFSVisit(G, v, l)
    u.c = VertexColor.BLACK
    time += u.t
    u.f = time
    l.append(u)


def TopologicalSort(G):
    l = []
    DFS(G, l)
    return l



if __name__ == "__main__":

    shoes = Vertex([], "shoes", 13 / 14)
    watch = Vertex([], "watch", 9 / 10)
    undershorts = Vertex([], "undershorts", 11/16)
    socks = Vertex([], "socks", 17 / 18)
    pants = Vertex([], "pants", 12/15)
    belt = Vertex([], "belt", 6/7)
    shirt = Vertex([], "shirt", 1/8)
    tie = Vertex([], "tie", 2/5)
    jacket = Vertex([], "jacket", 3 / 4)

    socks.a = [shoes]
    pants.a = [belt]
    belt.a = [jacket]
    shirt.a = [belt, tie]
    tie.a = [jacket]
    jacket.a = []
    undershorts.a = [pants, shoes]
    shoes.a = []
    watch.a = []

    G = [shirt, tie, jacket, belt, watch, undershorts, pants, shoes, socks]

    l = TopologicalSort(G)

    for i in l[::-1]:
        print(i.name)