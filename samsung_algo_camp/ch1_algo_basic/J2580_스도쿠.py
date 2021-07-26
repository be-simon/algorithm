# input
board = [list(map(int, input().split())) for _ in range(9)]

blank = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def check_blank(idx):
	if idx == len(blank):
		# print
		for i in range(9):
			print(' '.join(map(str,board[i])))
		exit()
		
	i, j = blank[idx]

	pi = (i // 3) * 3
	pj = (j // 3) * 3
	num_list = []
	for num in range(1, 10):
		pos = True
		for k in range(9): # 가로, 세로, 정사각형 구역에 하나라도 중복되면 불가능
			if board[i][k] == num or board[k][j] == num or board[pi + k // 3][pj + k % 3] == num:
				pos = False
				break
		if pos:
			num_list.append(num)

	for num in num_list:
		board[i][j] = num
		check_blank(idx + 1)
		board[i][j] = 0

			
check_blank(0)
