from collections import deque

def solution(begin, target, words):
    visited = {}
    graph = {}
    label = []#첫 시작 단어
    
    for word in words:
        conn = []
        for i,_ in enumerate(word):
            visited[word] = 0
            if check_word(word,begin,i) and not (word in label):#만약 begin과 한 글자 차이라면
                label.append(word)
            for x in words:#만약 word와 한 글자 차이라면
                if word != x and check_word(x,word,i):
                    conn.append(x)           
        graph[word] = conn
   
    queue = deque(label)
    depth_queue = deque([1] * len(label))#depth 저장

    while queue:
        word = queue.popleft()
        depth = depth_queue.popleft()
        if visited[word] == 0:#방문한 적이 없을 때
            visited[word] = 1
            if word == target:
                return depth
            queue += graph[word]
            depth_list = [depth+1] * len(graph[word])
            depth_queue+=depth_list
    
    return 0

def check_word(word,target,n):
    if word[n] != target[n]:
        for i,c in enumerate(target):
            if i != n and not (c == word[i]):
                return False
            
        return True
