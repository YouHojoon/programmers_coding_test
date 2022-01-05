import copy
from collections import deque
def solution(s):
    answer = 0
    min_len = 1001
    min_word = None
    
    for i in range(1,len(s)//2+2):
        words = deque()
        cnt = 1
        prev = None
        tmp = copy.copy(s)
        word = ""
        
        while True:#s를 간격대로 슬라이싱
            c = tmp[0:i]
            tmp = tmp[i:]
            words.append(c)
            

            if len(tmp) < i:
                if tmp != '':#마지막이 널문자가 아니라면
                    words.append(tmp)
                break
        
        # print(words)
        prev = words.popleft()
        while words:
            c = words.popleft()
            if prev == c:#같을 때
                cnt+=1;
            else:#다를 때
                if cnt != 1:
                    prev = str(cnt) + prev
                word += prev
                prev = c
                cnt = 1
                
        if cnt != 1:#마지막 글자
            prev = str(cnt) + prev
        word+=prev
        
        if len(word) < min_len:
            min_len = len(word)
            # print(word)
        
    return min_len
