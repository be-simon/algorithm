import sys
from collections import Counter

N = int(input())
narr = list(map(int, sys.stdin.readline().split()))
M = int(input())
marr = list(map(int, sys.stdin.readline().split()))

c = Counter(narr)
result = []
for m in marr:
    result.append(c[m])

print(' '.join(map(str, result)))
