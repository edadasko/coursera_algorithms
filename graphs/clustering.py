from collections import namedtuple

vertex = namedtuple('vertex', 'x y')
edge = namedtuple('edge', 'p1 p2 distance')


class DisjointSets:
    def __init__(self, n):
        self.size = n
        self.parents = [i for i in range(self.size)]
        self.rank = [0 for _ in range(self.size)]
    
    def union(self, i, j):
        destination, source = (i, j) if self.rank[i] > self.rank[j] else (j, i)
        
        parent_destination = self.find(destination)
        parent_source = self.find(source)
        
        if parent_destination == parent_source:
            return False
        
        if self.rank[destination] == self.rank[source]:
            self.rank[destination] += 1
        
        self.parents[parent_source] = parent_destination
        self.size -= 1
        return True
    
    def find(self, n):
        while n != self.parents[n]:
            n = self.find(self.parents[n])
        return n


def distance(v1, v2):
    return ((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2) ** (1 / 2)


def max_distance_between_clusters(n, count_of_clusters, edges):
    edges.sort(key=lambda d: d.distance)
    disjoint_sets = DisjointSets(n)
    for e in edges:
        if disjoint_sets.find(e.p1) != disjoint_sets.find(e.p2):
            disjoint_sets.union(e.p1, e.p2)
            if disjoint_sets.size < count_of_clusters:
                return e.distance


n = int(input())
vertexes = []
edges = []
for i in range(n):
    x, y = map(int, input().split())
    vertexes.append(vertex(x, y))

count_of_clusters = int(input())

for i in range(n):
    for j in range(i + 1, n):
        edges.append(edge(i, j, distance(vertexes[i], vertexes[j])))

print(str(max_distance_between_clusters(n, count_of_clusters, edges)))
