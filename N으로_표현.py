# 참고 : https://gurumee92.tistory.com/164
def solution(N, number):
    answer = -1
    dp = []
    
    for i in range(1,9):
        numbers = set()
        numbers.add(int(str(N) * i)) # 연속되는 수
        
        # 2번 써서 만들 수 있는 수
        # 1번 + 1번  
        # 3번 써서 만들 수 있는 수
        # 1번 + 2번
        # 2번 + 1번
        # 4번 써서 만들 수 있는 수
        # 1번 + 3번
        # 2번 + 2번
        # 3번 + 1번
        # ... N번 써서 만들 수 있는 수
        # 1번 + N-1번
        # 2번 + N-2번 ...
        
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0:
                        numbers.add(x // y)
                        
        if number in numbers:
            answer = i
            break
    
        dp.append(numbers)
        
    
    return answer
