from collections import deque

# input
N, L = map(int, input().split())
arr = list(map(int, input().split()))

answer = []
q = deque() # deque는 min-heap을 흉내낸다 (맨 앞 값이 구간의 최솟값)
for i in range(N):
	# 이번에 들어갈 숫자보다 큰 숫자들은 어짜피 최솟값이 되지 못한다.
	# 다 pop
	while q and q[-1] > arr[i]: 
		q.pop()
	
	q.append(arr[i]) # 이번에 들어갈 숫자 input

	# 만약 이번에 구간에서 나가는 숫자가 최솟값이라면 deque에서 빼준다
	if i >= L and q[0] == arr[i - L]:
		q.popleft()
	
	answer.append(q[0]) # deque의 맨 앞 숫자가 현재 구간에서의 최솟값

print(' '.join(map(str, answer)))
