def dfs(arr, visited, divisors,result):
    if len(arr) == 2 and arr not in result: # 2개를 선택한 모든 조합을 반환
        result.append(arr)
        return
    
    for i in range(0, len(divisors)):
        if visited[i] == 1:
            return
        
        if arr[0] >= divisors[i]:
            dfs(arr + [divisors[i]] ,visited, divisors,result)
    
def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    divisors = getDivisors(sum)
    result = []
    
    #하나면 경우의 수가 하나
    if len(divisors) == 1:
        return divisors * 2
    
    for i in range(1,len(divisors)):
        #가로가 세로와 같거나 커야하므로 가로보다 큰 약수는 1로 초기화
        dfs([divisors[i]],[0 if j <= i else 1 for j in range(len(divisors))], divisors,result)
        
    for item in result:
        if item[0] * item[1] == brown + yellow:
            brown_flag = item[0] * 2 + (item[1] - 2) * 2 # 테두리
            if brown_flag == brown_flag and sum - brown_flag == yellow:#테두리를 칠하고 남은것(중간)이 노란색과 같다면
                return item
        
    return answer


def getDivisors(n):
    arr = []
    for i in range(2, n):
        if n % i == 0:  
            arr.append(i)
    return arr
