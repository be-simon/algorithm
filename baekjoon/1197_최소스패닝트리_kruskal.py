from heapq import heappop, heappush
V, E = map(int, input().split())

h = []
parent = [i for i in range(V + 1)]

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    parent[pb] = pa

def isConnected(a, b):
    if find(a) == find(b):
        return 1
    else:
        return 0

for _ in range(E):
    a, b, c = map(int, input().split())
    heappush(h, (c, a, b))

union_cnt = 0
weight = 0
while h:
    c, a, b = heappop(h)
    if not isConnected(a, b):
        union(a, b)
        union_cnt += 1
        weight += c
    
    if union_cnt == V - 1:
        break

print(weight)
