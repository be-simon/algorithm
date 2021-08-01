import sys

input = sys.stdin.readline
inf = 100000000

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    dp = [[inf for _ in range(M + 1)] for _ in range(N + 1)]

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        g[u].append((v, c, d))

    dp[1][0] = 0
    for c in range(M + 1):
        for a in range(1, N + 1):
            if dp[a][c] == inf:
                continue

            for neigh, cost, dist in g[a]:
                ncost = c + cost
                ndist = dp[a][c] + dist
                if ncost > M:
                    continue
                if ndist < dp[neigh][ncost]:
                    dp[neigh][ncost] = ndist

    answer = min(dp[N])
    if answer == inf:
        print('Poor KCM')
    else:
        print(answer)
    