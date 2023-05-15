import Foundation

func solution(_ cap:Int, _ n:Int, _ deliveries:[Int], _ pickups:[Int]) -> Int64 {
    var result: Int64 = 0
    var deliveries = deliveries
    var pickups = pickups
    var toDeliveryIndex = deliveries.count - 1
    var toPickupIndex = pickups.count - 1
    
    
    while toDeliveryIndex != -1 || toPickupIndex != -1 {
        var remainCap = cap  
        var firstDeliveryIndex = -1
        var firstPickupIndex = -1
        
        //배달하러 가는 과정
        for i in stride(from: toDeliveryIndex, through: 0, by: -1){
            if deliveries[i] == 0{
                toDeliveryIndex = i - 1
                continue
            }
            
            // 배달해야되는 가장 먼 집을 만났을 때
            if firstDeliveryIndex == -1{
                firstDeliveryIndex = i
            }
            
            //배달이 모두 가능하면
            if deliveries[i] <= remainCap{
                remainCap -= deliveries[i]
                deliveries[i] = 0
                toDeliveryIndex = i - 1
            }
            //배달을 모두 할 수 없다면 
            else{
                deliveries[i] -= remainCap
                toDeliveryIndex = i 
                break
            }
        }
        
        remainCap = cap
        for i in stride(from: toPickupIndex, through: 0, by: -1){
            if pickups[i] == 0{
                toPickupIndex = i - 1
                continue
            }
            
            if firstPickupIndex == -1{
                firstPickupIndex = i
            }
           if pickups[i] <= remainCap{
               remainCap -= pickups[i]
               pickups[i] = 0
               toPickupIndex = i - 1
           }
           else{
               pickups[i] -= remainCap
               toPickupIndex = i
               break
           }
        }

        result += Int64(2 * (max(firstPickupIndex, firstDeliveryIndex) + 1))
    }

    return result
}
