def dfs(index,graph, visited):
    for i in range(len(graph[index])):
        if graph[index][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i, graph, visited)
 
def solution(n, wires):
    graph = [[0 for i in range(n + 1)] for i in range(n + 1)] 
    tmp_answer = []
    
    for x,y in wires:
        graph[x][y] = 1
        graph[y][x] = 1
        
    for i, wire in enumerate(wires):
        graph[wire[0]][wire[1]] = 0
        graph[wire[1]][wire[0]] = 0
        visited = [0 for i in range(n+1)] 
        depth = 1
        
        for i in range(1, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                dfs(i, graph, visited)
                break
       
        depth = sum(visited)
        tmp_answer.append(abs(n - 2* depth))
        graph[wire[0]][wire[1]] = 1
        graph[wire[1]][wire[0]] = 1

    return min(tmp_answer)
