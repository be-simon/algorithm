from collections import deque
N = int(input())
tx, ty = map(int, input().split())
r = int(input())
rel = {}

for _ in range(r):
    x, y = map(int, input().split())
    if x in rel:
        rel[x].append(y)
    else:
        rel[x] = [y]
    
    if y in rel:
        rel[y].append(x)
    else:
        rel[y] = [x]

queue = deque([(tx, 0)]) # person, chon
visit = [tx]
answer = 0
while queue:
    n, chon = queue.popleft()
    if n == ty:
        answer = chon

    if n in rel:
        for nxt in rel[n]:
            if nxt not in visit:
                queue.append((nxt, chon + 1))
                visit.append(nxt)

if answer == 0:
    answer = -1
print (answer)