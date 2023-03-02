import Foundation

struct Request: Comparable{
    var prior: Int
    var originIndex: Int
    
    public static func < (lhs: Self, rhs: Self) -> Bool {
        return lhs.prior < rhs.prior
    }
}

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var requests = priorities.enumerated().map{Request(prior:$1, originIndex:$0)} 
    var sortedPriorities = priorities.sorted(by: >)
    var result = 1
    
    while true{
        let firstRequest = requests.removeFirst()   
        
        if firstRequest.prior >= sortedPriorities[0]{   
            if location == firstRequest.originIndex{
                return result
            }
            _ = sortedPriorities.removeFirst()
            result += 1
        }
        else{
            requests.append(firstRequest)
        }
    }
    
    return 0
}


