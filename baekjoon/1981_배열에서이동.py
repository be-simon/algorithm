# dfs로 그래프 탐색
# 목적지로 가면서 최대-최소 값을 구해놓는다.
# 이미 구해둔 값보다 커지는 순간 그 경로는 폐기
import sys
input = sys.stdin.readline

n = int(input())
g = []
answer = [1000000000]

def dfs(i, j, minv, maxv):
    minv = min(minv, g[i][j])
    maxv = max(maxv, g[i][j])
    if maxv - minv >= answer[0]:
        return
    
    if (i, j) == (n-1, n-1):
        if maxv - minv < answer[0]:
            answer[0] = maxv - minv
        return

    v[i][j] = 1
    for _di, _dj in zip(di, dj):
        adi = i + _di
        adj = j + _dj
        if 0 <= adi < n and 0 <= adj < n and not v[adi][adj]:
            dfs(adi, adj, minv, maxv)

    v[i][j] = 0


for _ in range(n):
    g.append(list(map(int, input().split())))
v = [[0 for _ in range(n)] for _ in range(n)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

v[0][0] = 1


dfs(0, 0, g[0][0], g[0][0])
print(answer[0])