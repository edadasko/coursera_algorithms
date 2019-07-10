#Uses python3

import sys

def dfs(adj, node):
    is_visited[node] = True
    for n in adj[node]:
        if not is_visited[n]:
            dfs(adj, n)


def number_of_components(adj):
    result = 0
    for n in range(len(adj)):
        if not is_visited[n]:
            result += 1
            dfs(adj, n)
    return result


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
is_visited = [False for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
print(number_of_components(adj))
