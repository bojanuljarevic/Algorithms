from graf import *

def makeGraph():

    a = Graph.Node(val='a')
    b = Graph.Node(val='b')
    c = Graph.Node(val='c')
    d = Graph.Node(val='d')
    e = Graph.Node(val='e')
    f = Graph.Node(val='f')
    g = Graph.Node(val='g')
    h = Graph.Node(val='h')
    i = Graph.Node(val='i')
    G = Graph()
    G.insertNode(a).insertNode(b).insertNode(c).insertNode(d).insertNode(e)
    G.insertNode(f).insertNode(g).insertNode(h).insertNode(i)
    G.connectUndirected(a, b, 4)
    G.connectUndirected(a, h, 8)
    G.connectUndirected(b, c, 8)
    G.connectUndirected(b, h, 11)
    G.connectUndirected(c, i, 2)
    G.connectUndirected(c, d, 7)
    G.connectUndirected(c, f, 4)
    G.connectUndirected(d, e, 9)
    G.connectUndirected(d, f, 14)
    G.connectUndirected(f, g, 2)
    G.connectUndirected(g, h, 1)
    G.connectUndirected(g, i, 6)
    G.connectUndirected(h, i, 7)

    return G


if __name__ == "__main__":
    '''
    n1 = Node(val=1)
    n2 = Node(val=2)
    n3 = Node(val=3)
    n4 = Node(val=4)
    n5 = Node(val=5)

    n1.connect(n2).connect(n5)
    n2.connect(n1).connect(n3).connect(n5)
    n3.connect(n2).connect(n4)
    n4.connect(n3).connect(n5)
    n5.connect(n1).connect(n2).connect(n4)

    G = Graph()
    G.insertNode(n1)
    G.insertNode(n2)
    G.insertNode(n3)
    G.insertNode(n4)
    G.insertNode(n5)
    

    m1 = Graph.Node(val=1)
    m2 = Graph.Node(val=2)
    m3 = Graph.Node(val=3)
    m4 = Graph.Node(val=4)
    m5 = Graph.Node(val=5)
    m6 = Graph.Node(val=6)

    DAG = Graph()
    DAG.insertNode(m1)
    DAG.insertNode(m2)
    DAG.insertNode(m3)
    DAG.insertNode(m4)
    DAG.insertNode(m5)
    DAG.insertNode(m6)
    DAG.connectNodes(m1, m2)
    DAG.connectNodes(m1, m4)
    DAG.connectNodes(m5, m4)
    DAG.connectNodes(m2, m5)
    DAG.connectNodes(m4, m2)
    DAG.connectNodes(m3, m6)
    DAG.connectNodes(m6, m6)
    for i in DAG.Nodes:
        print("Node: ", i.val, "Neighbors: ", [node.val for node in i.adj])

    DAG.BFS(m1)
    for i in DAG.Nodes:
        print("Node: ", i.val, "Distance: ", i.d)
    
    DAG.printPath(m1, m5)

    DAG.DFS()
    
    #print([node.val for node in DAG.topologicalSort()])

    s = Graph.Node(val='s')
    t = Graph.Node(val='t')
    x = Graph.Node(val='x')
    y = Graph.Node(val='y')
    z = Graph.Node(val='z')

    G = Graph()
    G.insertNodes([s, t, x, y, z])
    G.connectNodes(s, t, 10)
    G.connectNodes(s, y, 5)
    G.connectNodes(t, x, 1)
    G.connectNodes(t, y, 2)
    G.connectNodes(x, z, 4)
    G.connectNodes(y, t, 3)
    G.connectNodes(y, x, 9)
    G.connectNodes(y, z, 2)
    G.connectNodes(z, s, 7)
    G.connectNodes(z, x, 6)
    
    G.Dijkstra(s)
    G.printPath(s, z)
    print("Distance: ", x.d)
    

    G = generateRandomGraph(4, 10)


    for i in G.Nodes:
        print("Node: ", i.val, "Neighbors: ", [node.val for node in i.adj])
    u = random.randint(0, len(G.Nodes)-1)
    u = G.Nodes[u]
    G.Dijkstra(u)
    for v in G.Nodes:
        print("Path from ", u.val, " to ", v.val)
        G.printPath(u, v)
    '''

    # Vjezba 11

    #G = makeGraph()
    #print(G.GetInDegrees())
    #print(G.GetOutDegrees())
    #print(G.ShortestPath(G.Nodes[0], G.Nodes[6]))
    #G.UpdateEdge(G.Nodes[1], G.Nodes[2], -6)
    #print(G.ShortestPath(G.Nodes[0], G.Nodes[6]))

    # Ispit primjer

    G = makeGraph()
    #G.ApplyStronglyConnectedComponents()
    G.Prim(G.Nodes[0])



