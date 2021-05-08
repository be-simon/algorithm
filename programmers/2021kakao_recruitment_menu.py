from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    food_cnt = Counter(''.join(orders))
    for c in course:
        food_cand = sorted([f for f, v in food_cnt.items() if v >= 2])
        
        if food_cand:
            food_course = []
            for fc in combinations(food_cand, c):
                fc = ''.join(fc)
                cnt = 0
                for o in orders:
                    if set(fc).issubset(set(o)):
                        cnt += 1
                if cnt >= 2:
                    if not food_course or cnt == food_course[0][1]:
                        food_course.append((fc, cnt))
                    elif cnt > food_course[0][1]:
                        food_course = [(fc, cnt)]
                
            for fc, cnt in food_course:
                answer.append(fc)

    
    return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]), ["AC", "ACDE", "BCFG", "CDE"])
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]), ["ACD", "AD", "ADE", "CD", "XYZ"])
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]), ["WX", "XY"])