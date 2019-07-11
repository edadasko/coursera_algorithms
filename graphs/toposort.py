def dfs(adj, node, is_visited, sorted_graph):
    is_visited[node] = True
    for n in adj[node]:
        if not is_visited[n]:
            dfs(adj, n, is_visited, sorted_graph)
    sorted_graph.append(node)


def toposort(adj):
    is_visited = [False for _ in range(n)]
    sorted_graph = []
    for node in range(n):
        if not is_visited[node]:
            dfs(adj, node, is_visited, sorted_graph)
    return reversed(sorted_graph)


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)

print(' '.join(map(str, [node + 1 for node in toposort(adj)])))
