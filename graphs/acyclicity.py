is_cycled = False

def dfs(adj, node):
    is_visited[node] = "in"
    for n in adj[node]:
        if is_visited[n] == "in":
            global is_cycled
            is_cycled = True
            return
        if not is_visited[n]:
            dfs(adj, n)
    is_visited[node] = True


def check_cycle(adj):
    for node in range(n):
        if not is_visited[node]:
            dfs(adj, node)


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
is_visited = [False for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
check_cycle(adj)
print(1 if is_cycled else 0)
