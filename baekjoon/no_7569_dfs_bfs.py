import sys
from collections import deque

M, N, H = map(int, input().split())
box = [[0 for _ in range(N)] for _ in range(H)]

for h in range(H):
    for n in range(N):
        box[h][n] = list(map(int, sys.stdin.readline().split()))

def check_mature():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 0:
                    return -1

dm = [1, 0, -1, 0, 0, 0]
dn = [0, -1, 0, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

queue = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue.append((h, n, m, 0)) # ( h, n, m, date )

cnt = 0
while queue:
    h, n, m, date= queue.popleft()
    cnt = date
    for _dh, _dn, _dm in zip(dh, dn, dm):
        adh = h + _dh
        adn = n + _dn
        adm = m + _dm
        if 0 <= adh < H and 0 <= adn < N and 0 <= adm < M:
            if box[adh][adn][adm] == 0:
                queue.append((adh, adn, adm, date + 1))
                box[adh][adn][adm] = 1

if check_mature() == -1:
    print(-1)
else:
    print(cnt)