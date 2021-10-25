import sys
import heapq
input = sys.stdin.readline # 여러줄 입력받을 때는 이걸로 시간을 줄여보자

N = int(input())
M = int(input())

inf = 100000000
d = [inf for _ in range(N + 1)]
cost = [[] for _ in range(N + 1)]

for _ in range(M):
  s, e, c = map(int, input().split())
  cost[s].append((e, c))

s, e = map(int, input().split())
h = []
heapq.heappush(h, (0, s))
d[s] = 0
while h:
  c, cur = heapq.heappop(h)
  if d[cur] < c: 
    continue

  for ad, adc in cost[cur]:
    nc = c + adc
    if nc < d[ad]:
      d[ad] = nc
      heapq.heappush(h, (d[ad], ad))

print(d[e])

