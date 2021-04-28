import sys
N = int(input())
E = int(input())

G = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    G[v1].append(v2)
    G[v2].append(v1)


queue = [1]
cnt = 0
while len(queue) > 0:
    node = queue.pop(0)
    visit[node] = 1
    for v in G[node]:
        if visit[v] == 0:
            visit[v] = 1
            cnt += 1
            queue.append(v)

print(cnt)