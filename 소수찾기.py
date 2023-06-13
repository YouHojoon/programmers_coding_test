def dfs(index,visited,arr, numbers, result):
    if arr[0] == '0':
        return
    
    if is_prime(int(arr)) and arr not in result:
        result.add(arr)
        
    for i in range(len(numbers)):
        if visited[i] == 0:
            visited[i] = 1
            
            dfs(i,visited,arr + str(numbers[i]), numbers, result)
            visited[i] = 0
      
            
            
def solution(numbers):
    answer = 0 
    numbers = list(map(int, numbers))
    result = set()
    visited = [0 for i in range(len(numbers))]
    
    for i in range(len(numbers)):
        visited[i] = 1
        dfs(i,visited, str(numbers[i]), numbers, result)
        visited[i] = 0
        
    print(result)
    return len(result)

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    
    return True
        
