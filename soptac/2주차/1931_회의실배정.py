import sys
input = sys.stdin.readline

N = int(input())

meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: [x[1], x[0]])

answer = 0
before_end = 0
for s, e in meetings:
    if before_end <= s:
        answer += 1
        before_end = e

print(answer)