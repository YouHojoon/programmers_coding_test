import Foundation

struct Queue<T>{
    var queue = [T]()
    
    mutating func pop() -> T?{
        return queue.isEmpty ? nil : queue.removeFirst()
    }
    
    mutating func push(_ element: T){
        queue.append(element)
    }
}


func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var queue = Queue<Int>()
    var result = [Int]()
    zip(progresses, speeds).forEach{ queue.push( Int(ceil(Double(100 - $0) / Double($1)))) }
    
    while let item = queue.pop(){
        var tmp = queue
        var cnt = 1
        
        while let nextItem = tmp.pop(), item >= nextItem{
            cnt+=1
        }
        
        for _ in 0 ..< cnt - 1{
            queue.pop()
        }
        
        queue.queue = queue.queue.map{$0 - item}
        result.append(cnt)
    }
    
    return result
}



