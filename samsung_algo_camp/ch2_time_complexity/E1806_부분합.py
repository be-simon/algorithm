N, S = map(int, input().split())

seq = list(map(int, input().split()))
s = 0
sum = 0
answer = 0

for e in range(N):
  sum += seq[e]

  while sum >= S:
    len = e - s + 1
    answer = len if answer == 0 else min(answer, len)
    sum -= seq[s]
    s += 1
    
print(answer)