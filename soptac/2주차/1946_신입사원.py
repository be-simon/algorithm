import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    cands = []
    for _ in range(N):
        cands.append(list(map(int, input().split())))
        
    answer = N
    cands = sorted(cands)
    minv = cands[0][1]
    for pap, itv in cands:
        if itv > minv:
            answer -= 1
        else:
            minv = itv
                    
    print(answer)                
        