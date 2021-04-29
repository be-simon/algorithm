import sys
from collections import deque

N, M = map(int, input().split())
tomato = []

for _ in range(M):
    tomato.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

empty = 0
cnt = 0
queue = deque([]) # (m, n, date)
day = []
for m in range(M):
    for n in range(N):
        if tomato[m][n] == -1:
            empty += 1
        elif tomato[m][n] == 1:
            queue.append((m, n, 0))
            cnt += 1

while len(queue) > 0:
    m, n, date = queue.popleft()
    day.append(date)
    for x, y in zip(dx, dy):
        adx = n + x
        ady = m + y
        if adx >= 0 and ady >= 0 and adx < N and ady < M:
            if tomato[ady][adx] == 0:
                queue.append((ady, adx, date + 1))
                tomato[ady][adx] = 1
                cnt += 1

if cnt + empty < M * N:
    print(-1)
else:
    print(day[-1])
