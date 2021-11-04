shorts = []
for _ in range(9):
    shorts.append(int(input()))
shorts.sort()


total = sum(shorts)
fake = []

isok = False
for i in range(9):
    if isok: 
        break
    for j in range(i + 1, 9):
        if total - (shorts[i] + shorts[j]) == 100:
            fake = [shorts[i], shorts[j]]
            isok = True
            break

for h in shorts:
    if h not in fake:
        print(h)