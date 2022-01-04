def solution(tickets):
    tickets.sort()#알파벳 순서가 앞서는 경로이므로 정렬
    visit = [False] * len(tickets)
    route = []
    dfs("ICN",tickets,route,len(tickets),visit)
    return route
  
    
def dfs(start,tickets,route,max,visit):
    route.append(start)
    
    if len(route) == max + 1:#경로를 찾은 경우
        return True
    
    for i,ticket in enumerate(tickets):
        ticket_start,ticket_dist = ticket
        if(start == ticket_start and not visit[i]):
            visit[i] = True
            if dfs(ticket_dist,tickets,route,max,visit):#연결된 곳까지 탐색
                return True#만약 성공이라면 반환
            else:
                visit[i] = False#실패라면 방문 취소
    
    route.pop(len(route)-1)#연결된 모든 곳을 탐색했지만 실패
    return False
            
    
        
