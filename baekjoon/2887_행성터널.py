import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
planets = []
parent = [i for i in range(N)]
h = []

def find(n):
    if parent[n] == n:
        return n

    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    pa = find(a)
    pb = find(b)
    parent[pb] = pa

def isConnected(a, b):
    if find(a) == find(b):
        return 1
    else:
        return 0


for i in range(N):
    planets.append([i] + (list(map(int, input().split()))))

for p in range(1, 4):
    planets.sort(key=lambda k: k[p])
    for i in range(len(planets)):
        if i == len(planets) - 1:
            j = i - 1
        else :
            j = i + 1

        d = abs(planets[i][p] - planets[j][p])
        cur = planets[i][0]
        to = planets[j][0]
        heappush(h, [d, cur, to])


answer = 0
union_cnt = 0
while h:
    d, cur, to = heappop(h)
    if union_cnt == 0:
        answer += d
        union(cur, to)
        union_cnt += 1
    elif isConnected(cur, to):
        continue
    else:
        answer += d
        union(cur, to)
        union_cnt += 1

    if union_cnt == N - 1:
        break

print(answer)



