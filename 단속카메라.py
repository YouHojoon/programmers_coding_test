# 참고 : https://wwlee94.github.io/category/algorithm/greedy/speed-enforcement-camera/
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    camera = routes[0][1] #진출 지점에 카메라를 설치
    answer = 1
    
    for route in routes[1:]:
         #다음 차량의 진입 지점이 카메라에 걸리지 않는다면 설치
        if camera < route[0]:
            answer += 1
            camera = route[1]
            
    return answer
