BLACK = 'black'
WHITE = 'white'


def is_bipartite(adj):
    colors = [None] * len(adj)
    return bfs(adj, colors)


def bfs(adj, colors):
    nodes = [0]
    colors[0] = BLACK
    is_visited[0] = True
    while nodes:
        n = nodes.pop(0)
        for node in adj[n]:
            if colors[node] and colors[node] == colors[n]:
                return False
            if not is_visited[node]:
                nodes.append(node)
                is_visited[node] = True
                colors[node] = BLACK if colors[n] == WHITE else WHITE
    return True


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
is_visited = [False for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
print('1' if is_bipartite(adj) else '0')
