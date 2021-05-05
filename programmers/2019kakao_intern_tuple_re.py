from collections import Counter
import re

def solution(s):
    c = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(c.items(), key=lambda x : x[1], reverse = True)]))