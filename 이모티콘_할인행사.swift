import Foundation

struct User{
    let discountRateBound: Int
    let priceBound: Int
}

func dfs(_ users: [User], _ emoticons:[Int], _ combination: [Int], _ discountRates: [Int]) -> [Int]{
    var result = [0,0]
    
    if combination.count == emoticons.count{
        //비교
        users.forEach{user in        
            let totalPrice = zip(emoticons, combination).reduce(0){(sum,combination) -> Int in
                let price = combination.0
                let discountRate = combination.1
                
		//연산 순서 다르면 틀릴 수 있다  
                return discountRate >= user.discountRateBound ?  sum + Int(Double(price) * (100.0 - Double(discountRate)) * 0.01) : sum
            }
            
            if user.priceBound <= totalPrice{
                result[0] += 1
            }
            else{
                result[1] += totalPrice
            }
        }
        return result
    }
    
    for discountRate in discountRates{
        let tmpResult = dfs(users, emoticons, combination + [discountRate], discountRates)
    
        if tmpResult[0] > result[0]{
            result = tmpResult
        }
        else if tmpResult[0] == result[0]{
            result = tmpResult[1] > result[1] ? tmpResult : result
        }
    }
    
    return result
}


func solution(_ users:[[Int]], _ emoticons:[Int]) -> [Int] {
    let users = users.map{User(discountRateBound:$0[0], priceBound:$0[1])}.sorted(by:{$0.discountRateBound > $1.discountRateBound})
    let discountRates = [10,20,30,40].filter{users.last!.discountRateBound <= $0}
    
    return dfs(users, emoticons, [], discountRates)
}

