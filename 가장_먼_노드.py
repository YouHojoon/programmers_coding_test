from collections import deque

#참고 : https://velog.io/@leejy1373/프로그래머스-BFS-가장-먼-노드-Python
def solution(n, edges):
    answer = 0
    #인접 행렬로 하게되면 시간초과
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)

    queue = deque([1])
    distance[1] = 0
    
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    while queue:
        cur = queue.popleft()
   
        for i in graph[cur]:
            if distance[i] == -1:                
                queue.append(i)
                distance[i] = distance[cur] + 1
    
    for i in range(1,n+1):
        if distance[i] == max(distance):
            answer += 1
    return answer
