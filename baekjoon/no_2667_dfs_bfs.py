import sys

G = []
N = int(input())
visit = [[0 for _ in range(N)] for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def adjacent(i, j):
    result = []
    for x, y in zip(dx, dy):
        adx = j + x
        ady = i + y
        if adx >= 0 and ady >= 0:
            if adx < N and ady < N:
                result.append((ady, adx))
    return result    

for _ in range(N):
    G.append(list((map(int, list(sys.stdin.readline())[:-1]))))
    
stack = []
result = []
for i in range(N):
    for j in range(N):
        if G[i][j] == 0:
            continue
        elif visit[i][j] == 0:
            cnt = 0
            # dfs
            stack.append((i, j))
            visit[i][j] = 1
            while len(stack) > 0:
                y, x = stack.pop()
                cnt += 1
                for ady, adx in adjacent(y, x):
                    if G[ady][adx] == 1 and visit[ady][adx] == 0:
                        visit[ady][adx] = 1
                        stack.append((ady, adx))
                        
            result.append(cnt)

result.sort()
print(len(result))
for n in result:
    print(n)
    