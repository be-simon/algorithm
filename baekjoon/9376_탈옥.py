import sys 
input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(jail, i, j, v, w, h):
    prisoner = 0
    open = 0

    if jail[i][j] == '$':
        prisoner += 1
    if jail[i][j] == '#':
        open += 1

    v[i][j] = 1
    for k in range(4):
        adi = i + di[k]
        adj = j + dj[k]
        if 0 <= adi < h and 0 <= adj < w and not v[adi][adj] and jail[adi][adj] != '*': 
            p, cnt = dfs(jail, adi, adj, v, w, h)
            
            

    return prisoner, open    


tc = int(input())
for _ in range(tc):
    h, w = map(int, input().split())
    jail = []
    start = []
    for i in range(h):
        l = list(input().strip())
        if l[0] in ['#', '.']: 
            start.append((i, 0))
        if l[-1] in ['#', '.']:
            start.append((i, w-1))
        if i == 0 or i == h-1:
            for j in range(1, w-1):
                if l[j] in ['#', '.']:
                    start.append((i, j))
            
        jail.append(l)

    for si, sj in start:
        v = [[0 for _ in range(w)] for _ in range(h)]
        print(dfs(jail, si, sj, v, w, h))

    print('---')
    