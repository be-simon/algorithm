import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

lake = []
q = deque()
sq = deque() # 백조의 현재 위치
wq = deque() # 얼음과 인접한 물의 위치
sv = [[0 for _ in range(c)] for _ in range(r)]
wv = [[0 for _ in range(c)] for _ in range(r)]

queue = deque([])
for i in range(r):
    l = list(input().strip())
    for j in range(c):
        if l[j] == 'L':
            sq.append((i, j))
            wq.append((i, j))
            wv[i][j] = 1
        elif l[j] == '.':
            wq.append((i, j))
            wv[i][j] = 1
    lake.append(l)

# bfs로 얼음을 녹인다
# bfs로 백조를 이동시킨다
#   if 만났다 -> return
# 이렇게 하면 얼음은 매번 V^2 탐색을 해야하고 백조는 매번 bfs를 다 돌아야함
#   전날 상태를 저장해주자.

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def swan():
    while q:
        i, j = q.popleft()
        if lake[i][j] == 'X':
            sq.append((i, j))
            continue
        for k in range(4):
            adi = i + di[k]
            adj = j + dj[k]
            if 0 <= adi < r and 0 <= adj < c and not sv[adi][adj]:
                if lake[adi][adj] == 'L':
                    return True
                
                q.append((adi, adj))
                sv[adi][adj] = 1
                
    return False

def water():
    while q:
        i, j = q.popleft()
        if lake[i][j] == 'X':
            lake[i][j] = '.'
            wq.append((i, j))
            continue
        for k in range(4):
            adi = i + di[k]
            adj = j + dj[k]
            if 0 <= adi < r and 0 <= adj < c and not wv[adi][adj] and lake[adi][adj] == 'X':
                    q.append((adi, adj))
                    wv[adi][adj] = 1

answer = 0
sq.popleft()
i, j = sq[0]
sv[i][j] = 1
while True:
    answer += 1

    q = wq
    wq = deque()
    water()
    
    q = sq
    sq = deque()
    if swan():
        print(answer)
        break