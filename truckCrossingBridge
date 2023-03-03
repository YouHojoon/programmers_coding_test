import Foundation
struct Queue<T>{
    var queue = [T]()
    
    mutating func push(_ element: T){
        queue.append(element)
    }
    mutating func pop() -> T?{
        return queue.isEmpty ? nil : queue.removeFirst()
    }
}

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    var queue = Queue<Int>()
    var bridge = Queue<Int>()
    var result = 0
    var bridgeLength = bridge_length
    truck_weights.forEach{queue.push($0)}
    var remainWeight = weight
    
    while true{
        result+=1
        
        if bridgeLength == bridge.queue.count{
            if let truck = bridge.pop(){
                remainWeight += truck
                remainWeight = min(remainWeight,weight)
                
                for i in 0 ..< bridge.queue.count{
                    if bridge.queue[0] == 0{
                        bridge.queue.removeFirst()
                    }
                    else{
                        break
                    }
                }
            }
            
            if bridge.queue.count == 0 && queue.queue.count == 0{
                return result
            }
        }
        
        if bridgeLength - bridge.queue.count > 0{
            if !queue.queue.isEmpty && queue.queue[0] <= remainWeight{
                if let truck = queue.pop(){
                    remainWeight -= truck
                    bridge.push(truck)
                }
            }
            else{
                bridge.push(0)   
            }
        }
    }
        
    
    return result
}



