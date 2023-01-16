import Foundation

func solution(_ distance:Int, _ rocks:[Int], _ n:Int) -> Int {
    var rocks = rocks + [distance]
    rocks.sort()
    var max = distance
    var min = 1
    var mid = 0
    
    while min<=max{
        mid = (max + min) / 2
        var removedCnt = 0
        var prev = 0
        
        for rock in rocks{
            if rock - prev < mid{
                removedCnt+=1
            }else{
                prev = rock    
            }
        }
        
        if removedCnt > n{
            max = mid - 1
        }
        else{
            min = mid + 1
        }
    }
     /*
        반복문이 종료됬다는 뜻 -> min이 max를 막 넘었다!
        min의 직전 위치인 max가 정답이다!
     */
    return max 
}


func getDistanceBetweenRock(_ rocks: [Int], _ index: Int, _ distance: Int) -> Int{
    if index == 0{
        return rocks[index]
    }
    else{
        return rocks[index] - rocks[index - 1]
    }
}


