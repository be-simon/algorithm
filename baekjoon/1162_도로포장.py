import sys
from heapq import heappush, heappop
from math import inf
input = sys.stdin.readline

N, M, K = map(int, input().split())

# dp[][] -> 1 ~ N까지 가는데 K개 포장을 써서 가는 최소값
dp = [[inf for _ in range(K + 1)] for _ in range(N + 1)]
g = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    g[s].append([e, t])
    g[e].append([s, t])

dp[1][0] = 0
h = [(0, 1, 0)] # time, cur, k
while h:
    time, city, kcnt = heappop(h)
    if dp[city][kcnt] < time:
        continue
    
    for e, t in g[city]:
        nt = time + t
        # 이번엔 포장 안함
        if nt < dp[e][kcnt]:
            dp[e][kcnt] = nt
            heappush(h, (nt, e, kcnt))
        
        # 이번에 포장하는 경우
        nt = time
        if kcnt < K and nt < dp[e][kcnt + 1]:
            dp[e][kcnt + 1] = nt
            heappush(h, (nt, e, kcnt + 1))

print(min(dp[N]))