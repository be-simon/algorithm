import sys
input = sys.stdin.readline

M, N = map(int, input().split())
friends = [int(input()) for _ in range(N)]

remain = sum(friends) - M
friends.sort()
fury = 0

for f in friends:
    candy = min(f, remain // N)
    fury += candy * candy
    remain -= candy
    N -= 1

print(fury % pow(2, 64))    