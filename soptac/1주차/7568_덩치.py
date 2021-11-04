import sys
input = sys.stdin.readline

N = int(input())

persons = []
for _ in range(N):
    x, y = map(int, input().split())
    persons.append((x, y))
    
for i in range(N):
    x1, y1 = persons[i]
    cnt = 0
    for j in range(N):
        x2, y2 = persons[j]
        if x2 > x1 and y2 > y1:
            cnt += 1
    print(cnt + 1)
