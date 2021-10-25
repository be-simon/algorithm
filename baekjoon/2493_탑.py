import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))

s = []
answer = []
for i in range(len(tops)):
    while s and tops[i] > tops[s[-1]]:
        s.pop()
    
    if not s:
        answer.append(0)
    else: 
        answer.append(s[-1] + 1)
    s.append(i)

print(' '.join(map(str, answer)))
    

