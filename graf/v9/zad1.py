
from vertex_example import *


if __name__ == "__main__":

    # GRAF 1

    v1 = Vertex([], 1)
    v2 = Vertex([], 2)
    v3 = Vertex([], 3)
    v4 = Vertex([], 4)
    v5 = Vertex([], 5)

    v1.a += [v2, v5]
    v2.a += [v1, v3, v4, v5]
    v3.a += [v2, v4]
    v4.a += [v2, v3, v5]
    v5.a += [v1, v2, v4]

    # GRAF 2

    v1 = Vertex([], 1)
    v2 = Vertex([], 2)
    v3 = Vertex([], 3)
    v4 = Vertex([], 4)
    v5 = Vertex([], 5)
    v6 = Vertex([], 6)

    v1.a += [v2, v4]
    v2.a += [v5]
    v3.a += [v5, v6]
    v4.a += [v2]
    v5.a += [v4]
    v6.a += [v6]