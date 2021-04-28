dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def solution(board):
    answer = 0
    N = len(board)
    memo = [[[0] for _ in range(N)] for _ in range(N)]    
    memo[0][1] = [100, (-1, 0)]
    memo[1][0] = [100, (0, -1)]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if (i, j) == (0, 1) or (i, j) == (1, 0):
                continue
            if board[i][j] == 0:
                # 인접 셀에서의 추가 비용 계산
                value = []
                for x, y in zip(dx, dy):
                    adx = j + x
                    ady = i + y
                    if adx >= 0 and adx < N and ady >= 0 and ady < N:
                        print(ady, adx)
                        if board[ady][adx] != 1 and memo[ady][adx][0] > 0:
                            if memo[ady][adx][1] == (x, y):
                                value.append([memo[ady][adx][0] + 100, (x, y)])
                            else:
                                value.append([memo[ady][adx][0] + 600, (x, y)])
                print(i, j, value)
                value.sort(key = lambda x: x[0])
                memo[i][j] = value[0]

    # print(memo)
    answer = memo[N - 1][N - 1][0]          
    return answer

# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 900)
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]), 3800)
