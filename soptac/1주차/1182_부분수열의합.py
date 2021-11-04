import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

answer = 0
for i in range(1, N + 1):
    for comb in combinations(numbers, i):
        if sum(comb) == S:
            answer += 1
print(answer)