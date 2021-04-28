import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N + 1)]
dfs_visit = [0 for _ in range(N + 1)]
bfs_visit = [0 for _ in range(N + 1)]
dfs_result = []
bfs_result = []

def DFS(i):
    dfs_visit[i] = 1
    dfs_result.append(i)
    for v in G[i]:
        if dfs_visit[v] == 0:
            DFS(v)

def BFS(i):
    queue = deque([])
    queue.append(i)
    while len(queue) > 0:
        node = queue.popleft()
        bfs_visit[node] = 1
        bfs_result.append(node)
        for v in G[node]:
            if bfs_visit[v] == 0:
                bfs_visit[v] = 1
                queue.append(v)


for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    G[v1].append(v2)
    G[v2].append(v1)

for g in G:
    g.sort()

DFS(V)
BFS(V)
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))