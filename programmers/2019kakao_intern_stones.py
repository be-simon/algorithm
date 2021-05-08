def solution(stones, k):
    answer = float('inf')
    i = 0
    j = k
    while j <= len(stones):
        mi = stones.index(max(stones[i:j]))
        print(mi)
        if stones[mi] < answer:
            answer = stones[mi]
        i = mi + 1
        j = i + k
    
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3), 3)