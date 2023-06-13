def dfs(depth,visited, k,dungeons,result):
    if depth == len(dungeons): #던전을 다 탐험했다면
        result.append(depth)
        
    for i in range(len(dungeons)):
        if visited[i] == 0:
            visited[i] = 1
            dungeon = dungeons[i]
            
            if dungeon[0] <= k:# 탐험을 할 수 있다면
                dfs(depth + 1, visited, k - dungeon[1], dungeons,result) #추가 탐험
                visited[i] = 0 #탐험이 끝남, 순서가 바뀔수도 있으므로 0으로 변경  
            else: #없다면
                result.append(depth)
                visited[i] = 0


def solution(k, dungeons):
    result = []
    visited = [0 for i in range(len(dungeons))]
    
    for i in range(len(dungeons)):
        dungeon = dungeons[i]
        if dungeon[0] <= k:
            visited[i] = 1
            dfs(1, visited, k - dungeon[1], dungeons, result)
            visited[i] = 0
        
    return max(result)
