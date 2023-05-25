from functools import reduce
# https://esoongan.tistory.com/103

def solution(numbers):
    answer = ""
    numbers = list(map(lambda x: str(x), numbers))
    numbers = sorted(numbers, key= lambda x: 3*x, reverse= True)
    
    return str(int(reduce(lambda x,y: x+y, numbers)))
    
