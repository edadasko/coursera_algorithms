from queue import PriorityQueue
INF = float('inf')

def distance(adj, cost, s, t):
    q = PriorityQueue()
    n = len(adj)
    min_costs = [INF] * n
    for i in range(n - 1):
        q.put((INF, i))
    q.put((0, s))
    min_costs[s] = 0
    for _ in range(len(adj) - 1):
        min_node = q.get()
        from_cost, from_node = min_node[0], min_node[1]
        for to_node in adj[from_node]:
            to_cost = from_cost + cost[from_node, to_node]
            if min_costs[to_node] > to_cost:
                min_costs[to_node] = to_cost
                q.put((to_cost, to_node))
    return min_costs[t] if min_costs[t] != INF else -1


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
cost = {}
for i in range(m):
    a, b, c = map(int, input().split())
    adj[a - 1].append(b - 1)
    cost[a - 1, b - 1] = c
s, t = map(int, input().split())
s, t = s - 1, t - 1
print(distance(adj, cost, s, t))
