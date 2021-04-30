from collections import deque
maxN = 100000
N, K = map(int, input().split())
visit = [0 for _ in range(maxN + 1)]

queue = deque([(N, 0)]) # (location, count)
while len(queue) > 0:
    n, cnt = queue.popleft()
    if n == K: # answer
        print(cnt)
        break
    nxt = [n - 1, n + 1, n * 2]
    for i in nxt:
        if 0 <= i <= maxN and visit[i] == 0:
            queue.append((i, cnt + 1))
            visit[i] = cnt + 1
