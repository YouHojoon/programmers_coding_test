import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var maxTime = times.reduce(0){$0 > $1 ? $0 : $1}
    var minRequireTime = 1
    var maxRequireTime = maxTime * n
    var peopleCount = 0
    var middleRequireTime = 0
    var result: Int64 = 0
    
    while minRequireTime <= maxRequireTime{
        middleRequireTime = (minRequireTime + maxRequireTime) / 2
        peopleCount = times.reduce(0){$0 + middleRequireTime / $1}
        
        if peopleCount < n{
            /*
                시간이 더 필요하다!
            */
            minRequireTime = middleRequireTime + 1
        }
        else{
            /*
                시간이 충분하다!
                하지만 같다고 해서 최소 시간은 아니므로 최소 시간동안 모든 인원이 심사슬 다 받을 수 있도록
                계속 탐색을 진행한다.
            */
            maxRequireTime = middleRequireTime - 1
        }
    }
    
    return Int64(minRequireTime)
}
