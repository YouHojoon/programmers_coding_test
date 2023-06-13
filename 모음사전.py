def solution(word):
    answer = 0
    
    for i, c in enumerate(word):
        answer += (5 ** (5 - i) - 1) / 4  * "AEIOU".index(c) + 1
        
    return answer
