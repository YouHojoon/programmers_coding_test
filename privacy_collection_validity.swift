import Foundation
struct Privacy{
    let index: Int
    let validDate: ValidDate
    static var privacyTypeDict = [String: Int]()
    
    init(_ startDate: String, _ type: String, _ index: Int){
        self.validDate = ValidDate(startDate, Privacy.privacyTypeDict[type]!)
        self.index = index
    }
    
    func isValid(_ today: String) -> Bool{
        let todayDate = ValidDate(today)
        
        return validDate > todayDate || todayDate == validDate
    }
}
struct ValidDate: Comparable, Equatable{
    let year: Int
    let month: Int
    let day: Int
    
    init(_ date: String){
        let date = date.split(separator: ".").map{String($0)}.map{Int($0)!}
        
       year = date[0]
       month = date[1]
       day = date[2]
    }
    
    init(_ startDate: String, _ term: Int){
       let startDate = startDate.split(separator: ".").map{String($0)}.map{Int($0)!}
        
       var year = startDate[0]
       var month = startDate[1] + term
       var day = startDate[2] - 1
        
        if day < 1{
            if month != 1{
                month -= 1
            }
            else{
                year -= 1
                month = 12
            }
             day = 28
        }
        
        if month > 12{
            year += month % 12 == 0 ? month / 12 - 1 : month / 12
            month = month % 12 == 0 ? 12 : month % 12
        }
        
        self.year = year
        self.month = month
        self.day = day
    }
    
    
    public static func <(lhs: Self, rhs: Self) -> Bool{
        if lhs.year != rhs.year{
            return lhs.year < rhs.year
        }
        
        else if lhs.month != rhs.month{
            return lhs.month < rhs.month
        }
        
        else{
            return lhs.day < rhs.day
        }
    }
    
    public static func ==(lhs: Self, rhs: Self) -> Bool{
       return lhs.year == rhs.year && lhs.month == rhs.month && lhs.day == rhs.day
    }
    
}

func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    Privacy.privacyTypeDict = terms.reduce([String: Int]()){
        let item = $1.split(separator: " ").map{String($0)}
        var dict = $0
        dict[item[0]] = Int(item[1])!
        return dict
    }
    
    let privacies = privacies.map{
        return $0.split(separator: " ").map{String($0)}
    }.enumerated().map{Privacy($0.1[0],$0.1[1],$0.0 + 1)}

    return privacies.filter{
        !$0.isValid(today)
    }.enumerated().map{$0.1.index}
}
