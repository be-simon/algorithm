import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
    
answer = 0
for c in coins[::-1]:
    if not K:
        break
    
    div = K // c
    if div:
        answer += div
        K %= c
        
print(answer)        