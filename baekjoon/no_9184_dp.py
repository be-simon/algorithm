m = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif m[a][b][c] > 0:
        return m[a][b][c]
    elif a < b and b < c:
        m[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        m[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return m[a][b][c]

while True:
    l = input()
    if l == '-1 -1 -1':
        break
    else:
        [a,b,c] = map(int, l.split())
        print('w({0}, {1}, {2}) = {3}'.format(a, b, c, w(a, b, c)))
