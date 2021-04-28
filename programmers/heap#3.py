import heapq

def solution(operations):
    heap = []
    heapq.heapify(heap)
    
    for o in operations:
        o = o.split(' ')
        if o[0] == 'I':
            heapq.heappush(heap, int(o[1]))
        elif o[0] == 'D':
            if o[1] == '1':
                heap.remove(max(heap))
            elif o[1] == '-1' and len(heap) > 0:
                heapq.heappop(heap)
                
    
    if len(heap) > 0:
        return [max(heap), min(heap)]
    else:
        return [0,0]


if __name__ == '__main__':
  # print(solution(["I 16","D 1"]), [0,0])
  print(solution(["I 7","I 5","I -5","D -1"]),	[7,5])