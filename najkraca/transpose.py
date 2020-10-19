from graph import *
import copy

def transposeGraph(G):
    tG = copy.deepcopy(G)
    for v in tG:
        v.e = []
    for v in G:
        for edge in v.e:
            for u in tG:
                if edge.dst.d2 == u.d2:
                    u.addEdge(edge.dst, edge.src, edge.w)
                    break
    return tG




if __name__ == "__main__":

    a = Vertex(VertexColor.GRAY)
    b = Vertex(VertexColor.WHITE)
    c = Vertex(VertexColor.WHITE)
    d = Vertex(VertexColor.WHITE)

    a.d2 = "a"
    b.d2 = "b"
    c.d2 = "c"
    d.d2 = "d"

    a.e.append(Edge(a, b, 10))
    a.e.append(Edge(a, c, 10))
    a.e.append(Edge(a, d, 10))
    b.e.append(Edge(b, c, 10))
    d.e.append(Edge(d, c, 10))

    G = [a, b, c, d]

    tG = transposeGraph(G)

    for v in tG:
        print(v.d2)
        for edge in v.e:
            print(edge.src.d2, edge.dst.d2)