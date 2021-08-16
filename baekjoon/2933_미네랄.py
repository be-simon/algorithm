import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

cave = []
for _ in range(r):
    cave.append(list(input().strip()))

n = int(input())
h = list(map(int, input().split())) if n > 1 else [int(input())]

di = [1, -1, 0, 0,]
dj = [0, 0, 1, -1]

# 클러스터를 찾는다
# 맨 밑 미네랄이면 리스트에 넣는다
# 맨 밑 미네랄들을 순회하면서 몇칸 떨어질 수 있는지 확인
# 미네랄들을 떨어뜨린다.    

def check_range(i, j):
    if 0 <= i < r and 0 <= j < c:
        return True
    else: return False

def get_dist(i, j, land):
    cnt = 0
    for k in range(i + 1, r):
        if land[k][j]:
            return cnt
        cnt += 1

    return cnt

def find_land_cluster():
    land = [[0 for _ in range(c)] for _ in range(r)]
    v = [[0 for _ in range(c)] for _ in range(r)]
    q = deque()

    for i in range(c):
        if cave[r-1][i] == 'x':
            q.append([r-1, i])
            v[r-1][i] = 1
            land[r-1][i] = 1

    while q:
        i, j = q.popleft()

        for k in range(4):
            adi = i + di[k]
            adj = j + dj[k]
            if check_range(adi, adj):
                if cave[adi][adj] == 'x' and not v[adi][adj]:
                    v[adi][adj] = 1
                    land[adi][adj] = 1
                    q.append([adi, adj])

    return land

def fall(cluster, dist):
    for i, j in cluster:
        cave[i + dist][j] = 'x'


def break_mineral(_i, _j):
    land = find_land_cluster()
    v = [[0 for _ in range(c)] for _ in range(r)]

    for k in range(4):
        adi = _i + di[k]
        adj = _j + dj[k]
        if check_range(adi, adj) and not v[adi][adj] and not land[adi][adj] and cave[adi][adj] == 'x':
            q = deque([[adi, adj]])
            cluster = [[adi, adj]]
            cave[adi][adj] = '.'
            bottom = []
            v[adi][adj] = 1
            while q:
                i, j = q.popleft()
                if i < r-1 and cave[i + 1][j] == '.':
                    bottom.append([i, j])
                for kk in range(4):
                    ii = i + di[kk]
                    jj = j + dj[kk]
                    if check_range(ii, jj) and not v[ii][jj] and cave[ii][jj] == 'x':
                        v[ii][jj] = 1
                        q.append([ii, jj])
                        cluster.append([ii, jj])
                        cave[ii][jj] = '.'

            d = 100
            for i, j in cluster:
                d = min(d, get_dist(i, j, land))

            fall(cluster, d)


for i in range(len(h)):
    for j in range(c):
        if i % 2 == 0:
            if cave[r - h[i]][j] == 'x':
                cave[r - h[i]][j] = '.'
                break_mineral(r-h[i], j)
                
                break
        elif cave[r - h[i]][c - j - 1] == 'x':
            cave[r - h[i]][c - j - 1] = '.'
            
            break_mineral(r-h[i], c-j-1)
            
            break

for l in cave:
    print(''.join(l))