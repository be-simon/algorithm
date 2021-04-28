from math import ceil

def solution(progresses, speeds):
  days = []
  for p, s in zip(progresses, speeds):
    days.append(ceil((100 - p) / s))

  cnt = 1
  answer = []
  for i in range(1, len(days)):
    if days[i] > days[i - 1]:
      answer.append(cnt)
    else:
      cnt += 1
  answer.append(cnt)

  return answer
  