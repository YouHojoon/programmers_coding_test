import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations:
        operator, operand = operation.split(" ")
        operand = int(operand)
        
        if operator == "I":
            heapq.heappush(min_heap, operand)
            heapq.heappush(max_heap, -operand)
            
        elif operator == "D":
            if len(min_heap) == 0:
                continue
                    
            else:
      
                if operand == 1:
                    value = heapq.heappop(max_heap)
                    min_heap.remove(-value)
                else:
                    value = heapq.heappop(min_heap)
                    max_heap.remove(-value)

    
    
    return [0,0] if len(min_heap) == 0 else [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
