import sys

sys.setrecursionlimit(200000)


def dfs(adj, node, is_visited, post_ordered=None):
    is_visited[node] = True
    for n in adj[node]:
        if not is_visited[n]:
            dfs(adj, n, is_visited, post_ordered)
    if post_ordered is not None:
        post_ordered.append(node)


def number_of_strongly_connected_components(adj, adj_rev, is_visited):
    result = 0
    post_ordered = []
    for node in range(len(adj)):
        if not is_visited[node]:
            dfs(adj_rev, node, is_visited, post_ordered)
    is_visited = [False for _ in range(len(adj))]
    for node in reversed(post_ordered):
        if not is_visited[node]:
            result += 1
            dfs(adj, node, is_visited)
    return result


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
adj_rev = [[] for _ in range(n)]
is_visited = [False for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj_rev[b - 1].append(a - 1)
print(number_of_strongly_connected_components(adj, adj_rev, is_visited))
