import sys
from collections import deque

# initialize
N, M = map(int, input().split())
miro = []
# crash / non-crash
visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
for _ in range(N):
    miro.append(list(map(int, sys.stdin.readline().rstrip('\n'))))

# move 
dm = [1, 0, -1, 0]
dn = [0, -1, 0, 1]

cnt = float('inf')
queue = deque([(0, 0, 1, 0)]) # n, m, cnt, crash
visit[0][0][0] = 1
while queue:
    _n, _m, _cnt, _crash = queue.popleft()

    if _n == N-1 and _m == M-1:
        if cnt > _cnt:
            cnt = _cnt
    
    for _dn, _dm in zip(dn, dm):
        adn = _n + _dn
        adm = _m + _dm
        if 0 <= adn < N and 0 <= adm < M: # valid range
            if _crash == 1 and visit[adn][adm][1] == 0: # already crashed
                if miro[adn][adm] == 0:
                    queue.append((adn, adm, _cnt + 1, _crash))
                    visit[adn][adm][1] = 1
            elif _crash == 0 and visit[adn][adm][0] == 0: # have chance to crash
                if miro[adn][adm] == 0:
                    queue.append((adn, adm, _cnt + 1, _crash))
                elif miro[adn][adm] == 1:
                    queue.append((adn, adm, _cnt + 1, _crash + 1))
                visit[adn][adm][0] = 1

if visit[N-1][M-1][0] == 1 or visit[N-1][M-1][1] == 1:
    print(cnt)
else:
    print(-1)