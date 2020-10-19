#include <stdio.h>
#include <stdlib.h>

enum COLOR
{
    WHITE,
    GRAY,
    BLACK
};

typedef struct vertex
{
    int key;
    enum COLOR color;
    int distance;
    struct vertex *parent;
} VERTEX;

typedef struct node
{
    VERTEX *v;
    struct node *next;
} NODE;

typedef struct
{
    VERTEX *v;
    NODE **adj;
} GRAPH;

GRAPH initGraph(int n)
{
    GRAPH g;

    g.v = calloc(n, sizeof(VERTEX));
    g.adj = calloc(n, sizeof(NODE *));

    return g;
}

NODE *createNode(VERTEX *v)
{
    NODE *node = malloc(sizeof(NODE));
    node->v = v;
    node->next = NULL;
    return node;
}

void addEdge(GRAPH *g, int x, int y)
{
    NODE *head = g->adj[x];
    NODE *newNode = createNode(&g->v[y]);

    if (head == NULL)
    {
        g->adj[x] = newNode;
    }
    else
    {
        NODE *tmp = head;
        while (tmp->next)
            tmp = tmp->next;
        tmp->next = newNode;
    }
}

NODE *enqueue(NODE *q, VERTEX *v)
{
    NODE *newNode = createNode(v);
    if (q == NULL)
    {
        q = newNode;
    }
    else
    {
        NODE *tmp = q;
        while (tmp->next)
            tmp = tmp->next;
        tmp->next = newNode;
    }

    return q;
}

VERTEX *dequeue(NODE **q)
{
    NODE *node = *q;
    *q = node->next;
    return node->v;
}

void bfs(GRAPH *g, int n, int s)
{
    int i;
    for (i = 0; i < n; i++)
    {
        g->v[i].key = i;
        g->v[i].color = WHITE;
        g->v[i].distance = -1;
        g->v[i].parent = NULL;
    }

    g->v[s].color = GRAY;
    g->v[s].distance = 0;
    NODE *q = NULL;
    q = enqueue(q, &(g->v[s]));

    while (q)
    {
        VERTEX *u = dequeue(&q);
        NODE *list = g->adj[u->key];

        while (list)
        {
            VERTEX *v = list->v;

            if (v->color == WHITE)
            {
                v->color = GRAY;
                v->distance = u->distance + 1;
                v->parent = u;
                q = enqueue(q, v);
            }

            list = list->next;
        }

        u->color = BLACK;
    }
}

int main()
{
    int n = 5;
    GRAPH g = initGraph(n);

    addEdge(&g, 0, 1);
    addEdge(&g, 1, 0);

    addEdge(&g, 0, 4);
    addEdge(&g, 4, 0);

    addEdge(&g, 4, 1);
    addEdge(&g, 1, 4);

    addEdge(&g, 2, 4);
    addEdge(&g, 4, 2);

    addEdge(&g, 3, 2);
    addEdge(&g, 2, 3);

    bfs(&g, n, 4);

    int i;
    for (i = 0; i < n; i++)
    {
        printf("key %d, dist %d\n", g.v[i].key, g.v[i].distance);
    }

    return 0;
}