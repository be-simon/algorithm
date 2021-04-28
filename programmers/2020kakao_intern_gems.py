def solution(gems):
    answer = []
    gemtype = set(gems)
    gemcnt = {}
    
    s = 0
    e = -1
    
    while e < len(gems) and s < len(gems):
        # print(gemcnt)
        # print(s, e)
        if len(gemcnt) != len(gemtype):            
            e += 1
            if e == len(gems):
                break
            gemcnt[gems[e]] = gemcnt.get(gems[e], 0) + 1  
        else:
            if gemcnt[gems[s]] == 1:
                answer.append([s + 1, e + 1])
                del gemcnt[gems[s]]
                s += 1
            else:
                gemcnt[gems[s]] -= 1
                s += 1
    
    answer.sort(key=(lambda x : (x[1] - x[0], x[0])))
    print(answer)
    return answer[0]

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]), [3, 7])
# print(solution(["AA", "AB", "AC", "AA", "AC"]), [1, 3])
# print(solution(["XYZ", "XYZ", "XYZ"]), [1, 1])
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]), [1, 5])
print(solution(["DIA", "EM", "EM", "RUB", "DIA"]), [3, 5])
