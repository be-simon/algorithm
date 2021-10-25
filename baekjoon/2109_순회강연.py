import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
data = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

heap = []
for p, d in data:
    heappush(heap, p)
    if len(heap) > d:
        heappop(heap)

print(sum(heap))