#참고 : https://life318.tistory.com/4, https://velog.io/@hyunjong96/프로그래머스-순위
def solution(n, results):
    answer = 0
    graph = [[0for _ in range(n+1)] for _ in range(n+1)] 
    
    for x,y in results:
        graph[x][y] = 1
        
    #floyd-warshall 
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if graph[i][j] == 0 and graph[i][k] and graph[k][j]:
                    # i가 k를 이기고 k가 j를 이긴다면 i는 j를 이긴다
                    graph[i][j] = 1
    
    column_sum = [0] * (n+1)
    row_sum = [0] * (n+1)
    
    for i in range(n+1):
        for j in range(n+1):
            column_sum[j] += graph[i][j]
            row_sum[i] += graph[i][j]
            
    for i in range(n+1):
        #나를 이긴 사람 + 내가 이긴사람이 n-1일때는 결과를 정확히 알 수 있다.
        if column_sum[i] + row_sum[i] == n-1:
            answer += 1
    return answer
