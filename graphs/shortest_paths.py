INF = float('inf')

def find_min_distances(source, adj, cost):
    # Bellman-Ford
    n = len(adj)
    dist = [INF] * n
    dist[source] = 0
    for _ in range(n - 1):
        for from_node in range(n):
            for to_node in adj[from_node]:
                dist[to_node] = relax_edge(dist, cost, from_node, to_node)
    neg_nodes = find_nodes_in_neg_cycle(adj, cost, dist)
    for n in neg_nodes:
        if dist[n] != -INF:
            dfs(adj, dist, n)
    return dist


def relax_edge(dist, cost, from_node, to_node):
    new_to_cost = dist[from_node] + cost[from_node, to_node]
    return new_to_cost if dist[to_node] > new_to_cost else dist[to_node]


def find_nodes_in_neg_cycle(adj, cost, dist):
    neg_cycle_nodes = []
    for from_node in range(len(adj)):
        for to_node in adj[from_node]:
            if dist[to_node] != relax_edge(dist, cost, from_node, to_node):
                neg_cycle_nodes.append(to_node)
    return neg_cycle_nodes


def dfs(adj, dist, neg_node):
    # for marked nodes that are reachable from node in negative cycle
    dist[neg_node] = -INF
    for to in adj[neg_node]:
        if dist[to] != -INF:
            dfs(adj, dist, to)


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
cost = {}
for i in range(m):
    a, b, c = map(int, input().split())
    adj[a - 1].append(b - 1)
    cost[a - 1, b - 1] = c
s = int(input()) - 1
dist = find_min_distances(s, adj, cost)
for d in dist:
    if d == INF:
        print('*')
    elif d == -INF:
        print('-')
    else:
        print(d)
