# 팰린드롬 (palindrome) - 앞뒤가 똑같은 수열
# 네이버 면접 때도 나왔음
import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())

dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

# def query(s, e):
#     if dp[s][e] > 0:
#         return dp[s][e]
    
#     if s == e:
#         dp[s][e] = 1
        
#     elif arr[s] == arr[e]:
#         if e - s <= 2:
#             dp[s][e] = 1
#         else:
#             dp[s][e] = query(s+1, e-1)
#     else:
#         dp[s][e] = 0
    
#     return dp[s][e]

for d in range(N):
    for s in range(1, N - d + 1):
        if not d:
            dp[s][s] = 1
        elif d == 1 or d == 2:
            dp[s][s+d] = 1 if arr[s] == arr[s+d] else 0
        else:
            dp[s][s+d] = dp[s+1][s+d-1] if arr[s] == arr[s+d] else 0
        

for _ in range(M):
    s, e = map(int, input().split())
    # print(query(s, e))
    print(dp[s][e])