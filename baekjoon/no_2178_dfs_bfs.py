import sys

N, M = map(int, input().split())
miro = []
visit = [[0 for _ in range(M)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    miro.append(list(map(int, sys.stdin.readline()[:-1])))

queue = [(0, 0)]
visit[0][0] = 1
while len(queue) > 0:
    x, y = queue.pop(0)
    for _x, _y in zip(dx, dy):
        adx = x + _x
        ady = y + _y
        if adx >= 0 and adx < M and ady >= 0 and ady < N:
            if miro[ady][adx] == 1 and visit[ady][adx] == 0:
                queue.append((adx, ady))
                visit[ady][adx] =  visit[y][x] + 1

print(visit[N - 1][M - 1])