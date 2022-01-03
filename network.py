def solution(n, computers):
    answer = 0
    for x in range(n):
        if dfs(x,computers):
            answer+=1
        
    return answer

def dfs(x,computers):
    if computers[x][x] == 0: #이미 방문했을 시 네트워크 개수는 0
        return False
    
    computers[x][x] = 0#자기 자신을 방문했다고 표시
    for i, n in enumerate(computers[x]):
        if n == 0:
            continue
        dfs(i,computers)#자신과 연결된 모든 컴퓨터를 방문
    
    return True#방문하지 않은 곳일 시
        
