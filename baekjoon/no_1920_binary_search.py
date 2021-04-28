import sys

N = int(sys.stdin.readline())
narr = [i for i in map(int, sys.stdin.readline().split())]
narr.sort()
M = int(sys.stdin.readline())
marr = [i for i in map(int, sys.stdin.readline().split())]

for m in marr:
    left = 0
    right = N - 1
    
    while left <= right:
        mid = (left + right) // 2
        if m < narr[mid]:
            right = mid - 1
        elif m > narr[mid]:
            left = mid + 1
        else:
            print(1)
            break
    
    if m != narr[mid]:
        print(0)
