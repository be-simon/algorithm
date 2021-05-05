def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    
    for m in moves:
        j = m - 1
        for i in range(n):
            if board[i][j] != 0:
                stack.append(board[i][j])
                board[i][j] = 0
                break
        if len(stack) > 1 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop()
            stack.pop()
                
    return answer