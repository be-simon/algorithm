def solution(s):    
    answer = []
    
    s = s[2:-2]
    subsets = [_s.split(',') for _s in s.split('},{')]
    subsets.sort(key=lambda x : len(x))

    for _sset in subsets:
        if len(answer) == 0:
            answer.append(_sset[0])
        else:
            # for a in answer:
            #     i.remove(a)
            # answer.append(i[0])
            for _s in _sset:
                if _s not in answer:
                    answer.append(_s)
                    break
    
    return list(map(int, answer))