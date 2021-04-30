from collections import deque

dx = [1, -1, 2, -2, 1, -1, 2, -2]
dy = [2, 2, 1, 1, -2, -2, -1, -1]
def move_night(x, y, n):
    result = []
    for _x, _y in zip(dx, dy):
        mx = x + _x
        my = y + _y
        if 0 <= mx < n and 0<= my < n:
            result.append((mx, my))
    return result

tc = int(input())
for _ in range(tc):
    I = int(input())
    cx, cy = map(int, input().split())
    tx, ty = map(int, input().split())
    visit = [[0 for _ in range(I)] for _ in range(I)]
    visit[cx][cy] = 1

    queue = deque([(cx, cy, 0)])
    while len(queue) > 0:
        x, y, cnt = queue.popleft()
        if (x, y) == (tx, ty):
            print(cnt)
            break

        for nx, ny in move_night(x, y, I):
            if visit[nx][ny] == 0:
                queue.append((nx, ny, cnt + 1))
                visit[nx][ny] = 1