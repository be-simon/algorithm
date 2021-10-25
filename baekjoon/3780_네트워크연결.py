import sys, os
# input = sys.stdin.readline
dir = os.getcwd() + '/b.in'
inputf = open(dir, 'r')
input = inputf.readline
f = open('output.txt', 'w')

T = int(input())

parent = []
leng = []

def find(n):
    pp, l = parent[n]
    if pp == n:
        return parent[n]
    
    ans, al = find(pp)
    parent[n] = [ans, l + al]
    
    return parent[n]

def union(i, j):
    pi = find(i)[0]
    pj = find(j)[0]
    parent[pi] = [pj, abs(pi - pj) % 1000]
    

for _ in range(T):
    N = int(input())
    parent = [[i, 0] for i in range(N + 1)]

    while True:  
        l = input().split()  
        if l[0] == 'O':
            break
        
        if l[0] == 'E':
            i = int(l[1])
            f.write(str(find(i)[1]) + '\n')
        
        elif l[0] == 'I':
            i, j = int(l[1]), int(l[2])
            union(i, j)