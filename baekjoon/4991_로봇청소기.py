from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    room = []
    robot = []
    dirty = []
    dirty_cnt = 0
    for i in range(h):
        l = list(input().strip())
        for j in range(w):
            if l[j] == 'o':
                robot = (i, j)
                l[j] = 0
            elif l[j] == '*':
                dirty.append((i, j))
                l[j] = dirty_cnt + 1
                dirty_cnt += 1 
        room.append(l)

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    def check_range(i, j):
        if 0 <= i < h and 0 <= j < w:
            return True
        else: return False

    cost = [[0 for _ in range(dirty_cnt + 1)] for _ in range(dirty_cnt + 1)]
    pos = [robot] + dirty

    for i, j in pos:
        _from = room[i][j]
        v = [[0 for _ in range(w)] for _ in range(h)]
        q = deque([(i, j, 0)])
        v[i][j] = 1
        while q:
            _i, _j, move = q.popleft()
            to = room[_i][_j]
            if type(to) == int and to > 0:
                cost[_from][to] = move

            for k in range(4):
                adi = _i + di[k]
                adj = _j + dj[k]
                if check_range(adi, adj) and not v[adi][adj] and room[adi][adj] != 'x':
                    q.append((adi, adj, move + 1))
                    v[adi][adj] = 1
    
    # for l in room:
    #     print(l)
    # print('---')
    # for c in cost:
    #     print(c)

    answer = -1
    flag = 1
    for i in range(1, dirty_cnt + 1):
        if not cost[0][i]:
            flag = 0
            
    if flag:
        for p in permutations([i for i in range(1, dirty_cnt + 1)]):
            sum = cost[0][p[0]]
            for i in range(dirty_cnt - 1):
                f = p[i]
                t = p[i + 1]
                sum += cost[f][t]
            
            answer = sum if answer == -1 else min(answer, sum)

    print(answer)


    