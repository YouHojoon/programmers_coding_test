# 참고 : https://www.ai-bio.info/programmers/1843

def solution(arr):
    numbers =  [int(x) for x in arr[::2]]
    operators =  [x for x in arr[1::2]]
    M,m = {}, {} # 최대 최소를 저장할 딕셔너리
    
    # i ~ i 까지 연산하는 결과는 자기 자신
    for i in range(len(numbers)):
        M[(i,i)] = numbers[i]
        m[(i,i)] = numbers[i]
    
    for d in range(1, len(numbers)):
        for i in range(len(numbers)):
            j = i + d
            
            if j >= len(numbers):
                continue
                
            tmp_M, tmp_m = [],[]
            
            # i ~ k-1 , k~j 까지 연산을 나눔
            for k in range(i+1, j+1):
                if operators[k-1] == "-":
                    tmp_max = M[(i,k-1)] - m[(k,j)] # 최대이려면 최대에서 최소를 빼야함
                    tmp_min = m[(i,k-1)] - M[(k,j)] # 최소이려면 최소에서 최대를 빼야함
                    tmp_M.append(tmp_max)
                    tmp_m.append(tmp_min)
                else:
                    tmp_max = M[(i,k-1)] + M[(k,j)] # 최대이려면 최대에서 최대를 더해야함
                    tmp_min = m[(i,k-1)] + m[(k,j)] # 최소이려면 최소에서 최소를 더해야함
                    tmp_M.append(tmp_max)
                    tmp_m.append(tmp_min)
                    
            M[(i,j)] = max(tmp_M) # i에서 j까지 연산을 할 때 최대
            m[(i,j)] = min(tmp_m) # i에서 j까지 연산을 할 때 최소

    return M[(0,len(numbers) - 1)] # 모든 연산을 하였을 때 최대
