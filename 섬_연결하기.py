#참고 : https://hoons-dev.tistory.com/82
def find(x, parent):
    if x != parent[x]:# 내 자신이 최상위가 아니라면
        parent[x] = find(parent[x],parent) #내 부모를 최상위로 변경
        
    return parent[x] # 최상위 노드 반환

def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])
    parent = [i for i in range(n)]
    answer = 0
    
    for x,y,cost in costs:
        lhs = find(x,parent)
        rhs = find(y,parent)
        
        if lhs != rhs:
            if lhs > rhs:
                parent[lhs] = rhs
            else:
                parent[rhs] = lhs
                
            answer += cost
    
    return answer
