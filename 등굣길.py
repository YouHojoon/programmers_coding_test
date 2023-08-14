import math
def solution(m, n, puddles):
    #물에 잠긴지역은 갈 수 없기 때문에 0 으로 초기화
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = 1
    
    for i in range(0,m):
        for j in range(0,n):
            if (1+i == 1 and 1+j ==1) or [1+i, 1+j] in puddles:
                continue
            
            #j+1, i+1에 도달할 수 있는 경로의 개수는 
            #해당 좌표의 위 칸에 도달할 수 있는 경로의 개수와 
            #왼쪽 칸에 도달할 수 있는 경로의 개수의 합이다.
            dp[j+1][i+1] = dp[j][i+1] + dp[j+1][i]
            
    return dp[n][m] % 1000000007
