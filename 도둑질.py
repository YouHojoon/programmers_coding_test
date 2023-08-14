#참고 : https://hbj0209.tistory.com/93
def solution(money):
    #dp = i까지 털었을 때의 최대값
    dp1 = [0] * len(money) # 반드시 첫번째 집을 터는 경우
    dp2 = [0] * len(money) # 반드시 마지막 집을 터는 경우
    
    dp1[0] = money[0] # 첫번째 집을 털었으므로
    dp1[1] = dp1[0] # 못털기 때문
    
    dp2[1] = money[1] #첫번째 집을 안털기 때문에
    
    for i in range(2, len(money)):
        # 지금 있는 곳을 털것인가 말것인가
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i]) 
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])    
    
    return max(dp1[-2], dp2[-1])
    
    

