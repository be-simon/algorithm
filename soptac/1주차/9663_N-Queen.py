# -*- encoding: utf-8 -*-

# 결국 다 해봐야된다.
# 1. N개를 다 놓고 체크한다.
#   N*N C N -> 재앙
#   N*N -> 찜찜함
# 2. 체크를 다 놓고 하지 말고 놓으면서 체크하기

# row마다 위치를 저장한다.
# 놓기 전에 이전 말들과 비교해서 가능한지 본다.


N = int(input())
pos = [0 for _ in range(N)]
answer = 0
def recur(cur):
    # if N개 다 놓음
    #   출력
    # else
    #   이전 말들과 비교
    #   놓을 수 있으면 go, 아니면 Return
    
    if cur == N:
        global answer
        answer += 1
        return
    
    for j in range(N): # 현재 줄에서 놓을 위치 선택
        isok = True
        for i in range(cur): # 이전 줄에 있는 말들
            if pos[i] == j or abs(pos[i] - j) == abs(i - cur):
                isok = False
                break
        if isok:
            pos[cur] = j
            recur(cur + 1)

recur(0)
print(answer)