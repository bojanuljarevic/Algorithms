from enum import Enum	

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, a = None, name = None, t = None, d = None, f = None, pi = None, c = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.pi = pi
        self.a = a
        self.d = d
        self.f = f
        self.name = name
        self.t = t

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.val = val
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
		



