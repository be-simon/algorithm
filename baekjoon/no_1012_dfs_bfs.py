import sys

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# get adjacent space
# check list range out
def adjacent(i, j, m, n):
    result = []
    for x, y in zip(dx, dy):
        adx = j + x
        ady = i + y
        if adx >= 0 and ady >= 0:
            if adx < m and ady < n:
                result.append((ady, adx))
    
    return result    

# solution
T = int(input())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    G = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        G[y][x] = 1
    
    stack = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] == 1 and visit[i][j] == 0:
                #DFS
                stack.append((i, j))
                visit[i][j] = 1
                while len(stack) > 0:
                    y, x = stack.pop()
                    for ady, adx in adjacent(y, x, M, N):
                        if G[ady][adx] == 1 and visit[ady][adx] == 0:
                            visit[ady][adx] = 1
                            stack.append((ady, adx))
                
                cnt += 1
    print(cnt)
            