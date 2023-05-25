import heapq

def solution(jobs):
    jobs.sort()
    queue = []
    sum = 0
    curr_time = 0
    n = len(jobs)
    for i in range(n):
        tmp = [(processing_time, request_time) for request_time, processing_time in jobs if request_time <= curr_time]
        
        if len(tmp) == 0:
            curr_time = jobs[0][0]
            tmp = [(processing_time, request_time) for request_time, processing_time in jobs if request_time <= curr_time]
            
        heapq.heapify(tmp)
        
        processing_time, request_time = heapq.heappop(tmp)
        jobs.remove([request_time, processing_time])
        sum += curr_time - request_time + processing_time
        curr_time += processing_time
        
    return sum // n
