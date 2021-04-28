import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
cnt = 0
for _ in range(N):
    coins.append(int(input()))

while len(coins) > 0:
    c = coins.pop()
    if K // c > 0:
        cnt += K // c
        K %= c

print(cnt)