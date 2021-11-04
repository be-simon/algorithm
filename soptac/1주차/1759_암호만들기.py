# -*- coding: utf-8 -*-
# if bruteforce
# C개의 문자를 가지고 가능한 암호를 모두 만들어본다.
#   -> 규칙에 맞는지 확인한다 (자음 2개 모음 1개)
#   -> 생각해보면 최대 15C7 = 6435

import sys
input = sys.stdin.readline

L, C = map(int, input().split())
chars = list(input().split())

chars.sort()

from itertools import combinations

def check(iter):
    mo, ja = [0, 0]
    for c in iter:
        if c in ['a', 'e', 'i', 'o', 'u']:
            mo += 1
        else: 
            ja += 1
    
    if mo >= 1 and ja >= 2:
        return True
    else: return False

combs = combinations(chars, L)
for comb in combs:
    if check(comb):
        print(''.join(comb))    
    

# ---------------
# a, c, i, s, t, w
# ac, ai, as, at, aw
# aci, acs, act, acw
# acis, acit, aciw

def get_pw(cur, answer, mo):
    # if 4자리
    #   if ok -> print
    #   else -> return
    # else
    #   자음 모음 개수 늘리고 자식으로 넘어감
    if len(answer) == L:
        if mo >= 1 and len(answer) - mo >= 2:
            print(answer)    
        return
    
    for i in range(cur, C):
        if chars[i] in ['a', 'e', 'i', 'o', 'u']:
            get_pw(i + 1, answer +  chars[i], mo + 1)
        else:
            get_pw(i + 1, answer +  chars[i], mo)
        
get_pw(0, '', 0)    