import sys
input = sys.stdin.readline

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

op = {0:5, 1:3, 2:4, 3:1, 4:2,5:0}
answer = 0

for bi in range(6):
    ms = 0
    ti = op[bi]
    k = dices[0][ti]
    mside = 0
    for i in [si for si in range(6) if si not in [ti, bi]]:
        mside = max(mside, dices[0][i])
    ms += mside
    
    for di in range(1, n):
        for i in range(6):
            if dices[di][i] == k:
                bottom = i
                break
        top = op[bottom]
        k = dices[di][top]
        mside = 0
        for i in [si for si in range(6) if si not in [top, bottom]]:
            mside = max(mside, dices[di][i])
        ms += mside    

    answer = max(answer, ms)

print(answer)


    