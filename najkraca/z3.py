from z2 import *
import random

def PrintPath(G, s, v):
    if v == s:
        print(s.d1)
    elif v.p == None:
        print("No path from vertices exists.")
    else:
        PrintPath(G, s, v.p)
        print(v.d1)


if __name__ == "__main__":

    G = []

    for i in range(random.randint(3, 5)):
        name = "v" + str(i)
        G.append(Vertex(VertexColor.WHITE, None, None, name))

    for v in G:

        for i in range(0, 10):

            u = G[random.randint(0,len(G)-1)]

            connected = False

            for edge in v.e:
                if edge.dst == u:
                    connected = True

            if connected == False:
                v.e.append(Edge(v, u, random.randint(0, 20)))



    for i in G:
        print("cvor")
        print(i.d2)
        print("susjedi")
        for j in i.e:
            print(j.dst.d2, j.w)

