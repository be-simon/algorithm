def solution(name):
    no_a = []
    answer = 0
    for i in range(len(name)):
        if name[i] != 'A':
            no_a.append(i)
            move = ord(name[i]) - ord('A') if name[i]  < 'N' else ord('A') + 26 - ord(name[i])
            answer += move

    if len(no_a) == len(name):
        return answer + len(name) - 1
    
    c = 0
    d = 0
    while len(no_a) > 0:
        
        if d == 0:
          f = no_a[0] - c
          b = len(name) - no_a[-1] + c
        else:
          f = c - no_a[-1]
          b = len(name) - c + no_a[0]

        if f <= b:
            answer += f
            
        else:
            answer += b
            d = (-1 if d == 0 else 0)
            
        c = no_a[d]
        no_a.pop(d)
    return answer

if __name__ == '__main__':
  print(solution("BBBAAAB"), 8)
  print(solution("ABABAAAAABA"), 10)
  print(solution("CANAAAAANAN"), 48) #48
  print(solution("ABABAAAAAB"), 8) #8
  print(solution("BABAAAAB"), 7) #7
  print(solution("AAA"), 0) #0
  print(solution("ABAAAAAAABA"), 6) #6
  print(solution("AAB"), 2) #2
  print(solution("AABAAAAAAABBB"), 11) #11
  print(solution("ZZZ"), 5) #5
  print(solution("BBBBAAAAAB"), 10) #10
  print(solution("ABAAAAABAB"), 8) #8
  print(solution("BBBBAAAABA"), 12) #12