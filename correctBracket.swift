import Foundation

struct Stack<T>{
    var stack = [T]()
    mutating func pop() -> T?{
        return stack.isEmpty ? nil : stack.popLast()
    }
    mutating func push(_ element: T){
        stack.append(element)
    }
}


func solution(_ s:String) -> Bool
{
    var ans:Bool = true
    var stack = Stack<Character>()
    
    for c in s{
        if c == "("{
            stack.push(c)
        }
        else{
            if stack.pop() == nil{
                ans = false
            }
        }
    }
    
    if stack.pop() != nil{
        ans = false
    }
    
    return ans
}
