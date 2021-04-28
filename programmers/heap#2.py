import heapq

def solution(jobs):
    # 일단 먼저 들어온 일을 실행한다
    # 일이 끝난 시점에서 쌓여있던 일들 중에 가장 짧은 것부터 처리한다
    # heap을 두개 운영?
    
    heapq.heapify(jobs) # 먼저 온 순서
    sched = []
    heapq.heapify(sched) # 스케줄러
    time = 0
    total = 0
    length = len(jobs)
    while True: 
        # 현재 시간까지 도착한 일들을 스케줄러에
        while len(jobs) > 0:
            come = heapq.heappop(jobs)
            if come[0] <= time:
                heapq.heappush(sched, (come[1], come[0]))
            else:
                heapq.heappush(jobs, come)
                break
        # 스케줄러에서 다음 테스크 실행
        if len(sched) > 0:
            next = heapq.heappop(sched)
            total += time - next[1] + next [0]
            time += next[0]
        elif len(jobs) >  0:
            next = heapq.heappop(jobs)
            time += next[0] - time + next[1]
            total += next[1]
        else:
          break
        # print('jobs: ', jobs)
        # print('sched: ', sched)
        # print('time: ', time)
        # print('total: ', total)
        
    answer = total // length
    return answer

if __name__ == '__main__':
  print(solution([[0, 3], [1, 9], [2, 6]]), 9)
  print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
  print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)
  print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]), 13)