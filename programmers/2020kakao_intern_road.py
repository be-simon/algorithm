from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(board):
    N = len(board)
    visit = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    
    queue = deque([[0, 0, 0, -1]]) # x, y, cost, dir
    while len(queue) > 0:
        x, y, cost, drt = queue.popleft()
        # print(x, y, cost, drt)
        if (x, y) == (N - 1, N - 1):
            result.append(cost)
            continue
            
        for i in range(len(dx)):
            adx = x + dx[i]
            ady = y + dy[i]
            if 0 <= adx < N and 0 <= ady < N and board[ady][adx] == 0:
                _cost = cost
                if drt == -1 or (drt - i) % 2 == 0:
                    _cost += 100    
                else:
                    _cost += 600
                    
                if visit[ady][adx] == 0 or visit[ady][adx] >= _cost:
                    queue.append([adx, ady, _cost, i])
                    visit[ady][adx] = _cost
    
    print(result)
    result.sort()
    return result[0]

# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 900)
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]), 3800)
