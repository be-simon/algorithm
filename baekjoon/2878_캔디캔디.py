import sys
input = sys.stdin.readline

m, n = map(int, input().split())

friends = [int(input()) for _ in range(n)]

friends = sorted(friends)
remain_candies = sum(friends) - m
total_furi = 0

for f in friends:
    c = min(f, remain_candies // n)
    total_furi += c * c
    remain_candies -= c
    n -= 1

print(total_furi % pow(2, 64))

