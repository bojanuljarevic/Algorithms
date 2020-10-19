from enum import Enum	

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None, e = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.d1 = d1
        self.d2 = d2
        self.e = []

    def addEdge(self, src, dst, w):
        self.e.append(Edge(src, dst, w))
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255


class Edge:

    def __init__(self, src = None, dst = None, w = None):

        self.src = src
        self.dst = dst
        self.w = w
		
u = Vertex(c=VertexColor.WHITE, d1=1, d2=22)
v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)




