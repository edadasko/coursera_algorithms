def check_node_for_negative_cycle(adj, cost):
    # Bellman-Ford
    n = len(adj)
    dist = [0] * n
    for _ in range(n - 1):
        for from_node in range(n):
            for to_node in adj[from_node]:
                dist[to_node] = relax_edge(dist, cost, from_node, to_node)

    for from_node in range(n):
        for to_node in adj[from_node]:
            if dist[to_node] != relax_edge(dist, cost, from_node, to_node):
                return True
    return False


def relax_edge(dist, cost, from_node, to_node):
    new_to_cost = dist[from_node] + cost[from_node, to_node]
    return new_to_cost if dist[to_node] > new_to_cost else dist[to_node]


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
cost = {}
is_visited = [False] * n
for i in range(m):
    a, b, c = map(int, input().split())
    adj[a - 1].append(b - 1)
    cost[a - 1, b - 1] = c


print('1' if check_node_for_negative_cycle(adj, cost) else '0')
