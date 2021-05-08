import heapq
INF = float('inf')

def dijkstra (n, s, e, G):
    D = [INF for _ in range(n + 1)]
    D[s] = 0
    queue = []
    heapq.heappush(queue, (0, s))

    while queue:
        d, v = heapq.heappop(queue)
        if v == e:
            return D[e]
        elif D[v] < d:
            continue
        else:
            for nv, w in G[v]:
                if D[nv] > d + w:
                    D[nv] = d + w
                    heapq.heappush(queue, (d + w, nv))
    
    return D[e]
    
def solution(n, s, a, b, fares):
    G = [[] for _ in range(n + 1)]
    for f in fares:
        G[f[0]].append((f[1], f[2]))
        G[f[1]].append((f[0], f[2]))
    
    answer = INF
    for i in range(1, n+1):
        fare = dijkstra(n, s, i, G) + dijkstra(n, i, a, G) + dijkstra(n, i, b, G)
        answer = min(answer, fare)        
    
    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))