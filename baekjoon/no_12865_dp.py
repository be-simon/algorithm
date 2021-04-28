import sys
N, K = map(int, sys.stdin.readline().split())
V = [0]
W = [0]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# def knapsack(n, k):
#     if dp[n][k] > 0:
#         return dp[n][k]
    
#     if n == 1:
#         if W[n] > k:
#             dp[n][k] = 0
#         else:
#             dp[n][k] = V[n]
#     elif W[n] > k:
#         dp[n][k] = knapsack(n-1, k)
#     else:
#         dp[n][k] = max(knapsack(n-1, k - W[n]) + V[n], knapsack(n-1, k))
    
#     return dp[n][k]

# for _ in range(N):
#     (w, v) = map(int, sys.stdin.readline().split())
#     V.append(v)
#     W.append(w)

# print(knapsack(N, K))

for _ in range(N):
    (w, v) = map(int, sys.stdin.readline().split())
    V.append(v)
    W.append(w)

for i in range(N + 1):
    for j in range(K + 1):
        if i == 1:
            if W[i] > j:
                dp[i][j] = 0
            else:
                dp[i][j] = V[i]
        elif W[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - W[i]] + V[i], dp[i - 1][j])

print(dp[i][j])

