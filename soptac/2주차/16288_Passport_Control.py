import sys
input = sys.stdin.readline

N, K = map(int, input().split())
passengers = list(map(int, input().split()))

queues = [0 for _ in range(K)]
answer = 'YES'
for p in passengers:
    isok = False
    for i in range(K):
        if queues[i] < p:
            queues[i] = p
            isok = True
            break
    if not isok:
        answer = 'NO'
        break

print(answer)
