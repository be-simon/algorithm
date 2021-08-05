from heapq import heappop, heappush

V, E = map(int, input().split())

g = [[] for _ in range(V + 1)]
connected = [0 for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    g[a].append([c, b])
    g[b].append([c, a])

h = []
heappush(h, [0, 1])
answer = 0
cnt = 0
while h:
    c, node = heappop(h)
    if connected[node]:
        continue

    connected[node] = 1
    cnt += 1
    answer += c

    if cnt == V:
        break

    for edge in g[node]:
        heappush(h, edge)

print(answer)
