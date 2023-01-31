import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dict = [String:Int]()
    var result = 1
    
    for cloth in clothes{
        dict[cloth[1]] = dict[cloth[1], default: 0] + 1
    }
    
    for key in dict.keys{
        result *= (dict[key]! + 1) // 옷을 고르는 경우의 수, 고르지 않는 경우도 있으므로 + 1
    }

    return result - 1 // 아무것도 안고르는 경우의 수도 있으므로 - 1
}

