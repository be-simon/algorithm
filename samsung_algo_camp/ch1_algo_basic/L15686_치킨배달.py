from itertools import combinations

n, m = map(int, input().split())
home = []
chickens = []

for i in range(n):
  tl = input().split()
  for j in range(n):
    if tl[j] == '1':
      home.append((i, j))
    elif tl[j] == '2':
      chickens.append((i, j))

def get_chic_dist(h, c):
  return abs(h[0] - c[0]) + abs(h[1] - c[1])

answer = -1
for chic_case in combinations(chickens, m):
  # 치킨집을 고른 케이스 별로
  sum = 0
  for h in home: # 집집 마다 치킨거리를 구한다.
    mind = -1
    for c in chic_case:
      d = get_chic_dist(h, c)
      mind = d if mind == -1 else min(mind, d)
    sum += mind

  answer = sum if answer == -1 else min(answer, sum)  
  
print(answer)

