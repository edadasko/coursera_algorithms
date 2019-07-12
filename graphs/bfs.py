def min_path(adj, from_node, to_node):
    if from_node == to_node:
        return 0
    min_paths = bfs(adj, from_node)
    return min_paths[to_node] if min_paths[to_node] else -1

def bfs(adj, from_node):
    min_paths = [0] * len(adj)
    is_visited[from_node] = True
    nodes = [from_node]
    while nodes:
        n = nodes.pop(0)
        for node in adj[n]:
            if not is_visited[node]:
                nodes.append(node)
                is_visited[node] = True
                min_paths[node] = min_paths[n] + 1
    return min_paths


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
is_visited = [False for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
from_n, to_n = map(int, input().split())
from_n, to_n = from_n - 1, to_n - 1
print(str(min_path(adj, from_n, to_n)))
