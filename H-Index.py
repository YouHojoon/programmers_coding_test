def solution(citations):
    citations = sorted(citations)
    
    for i,h in enumerate(citations):
        # 오름차순이기 때문에 h 이상임을 보장
        if h >= len(citations) - i:
            return len(citations) - i
    
    return 0
