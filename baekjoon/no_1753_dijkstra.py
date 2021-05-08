import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
G = [[] for _ in range(V + 1)]
D = [float('inf') for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u].append((v, w))

queue = []
D[start] = 0
heapq.heappush(queue, (0, start))
while queue:
    d, cv = heapq.heappop(queue)
    if D[cv] < d:
        continue

    for v, w in G[cv]:
        if d + w < D[v]:
            D[v] = d + w
            heapq.heappush(queue, (D[v], v))

for i in range(1, V+1):
    if D[i] == float('inf'):
        print('INF')
    else:
        print(D[i])


