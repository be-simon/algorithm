import sys
input = sys.stdin.readline

T = int(input())
parent = dict()
fn = dict()

def find(f):
    if parent[f] == f:
        return f
    
    root = find(parent[f])
    parent[f] = root
    return root

def union(f1, f2):
    p1 = find(f1)
    p2 = find(f2)
    
    if p1 != p2:
        parent[p2] = p1
        fn[p1] += fn[p2]
    print(fn[p1])

for _ in range(T):
    F = int(input())
    parent = dict()
    fn = dict()
    for _ in range(F):
        friends = input().split()
        for f in friends:
            if f not in parent:
                parent[f] = f
                fn[f] = 1
            
        union(friends[0], friends[1])
        
        
