import Foundation

func solution(_ gameBoard:[[Int]], _ table:[[Int]]) -> Int {
    var result = 0
    var gameBoard = gameBoard
    var blocks = findBlocks(table)
    
    for _ in 0 ..< 4{
        gameBoard = rotate(gameBoard)
        var tmpGameBoard = gameBoard
        
        for i in 0..<gameBoard.count{
            for j in 0..<gameBoard[0].count{
                if tmpGameBoard[i][j] == 0{
                    tmpGameBoard[i][j] = 2
                    let holes = dfs(&tmpGameBoard,x:j, y:i, checkNum:0, prevMove: (0,0))
                    
                    if let blockIndex = blocks.firstIndex(where:{canPutBlockInHole($0, holes)}){
                        let block = blocks[blockIndex]
                        blocks.remove(at:blockIndex)
                        result += block.count
                        gameBoard = tmpGameBoard
                    }
                    else{
                        tmpGameBoard = gameBoard
                    }
                }
            }
        }
    }
    
    return result
}

func canPutBlockInHole(_ blocks:[(Int, Int)], _ holes: [(Int, Int)]) -> Bool{
    if blocks.count != holes.count{
        return false
    }
                        
    for (index,block) in blocks.enumerated(){
        if block.0 != holes[index].0 || block.1 != holes[index].1{
            return false
        }
    }
    return true
}
func findBlocks(_ table: [[Int]]) -> [[(Int,Int)]]{
    var blocks = [[(Int,Int)]]()
    var table = table
    for i in 0..<table.count{
        for j in 0..<table[0].count{
            if table[i][j] == 1{
                table[i][j] = 2
                blocks.append(dfs(&table,x:j,y:i, checkNum: 1, prevMove:(0,0)))
            }
        }
    }
    return blocks
}

func dfs(_ list: inout [[Int]], x:Int, y:Int, checkNum: Int,prevMove: (Int, Int)) -> [(Int,Int)]{
    let points = [(1,0),(0,1),(-1,0),(0,-1)]
    var result = [prevMove]
    for point in points{
        let newX = x + point.0
        let newY = y + point.1
        
        if (newX >= 0 && newX < list[0].count) && (newY >= 0 && newY < list.count) && list[newY][newX] == checkNum{
            list[newY][newX] = 2         
            result += dfs(&list, x: newX, y: newY, checkNum: checkNum, prevMove: (prevMove.0 + point.0, prevMove.1 + point.1))
        }
    }
    
    return result
}
func rotate(_ list: [[Int]]) -> [[Int]]{
    var result = list
    for i in 0..<list.count{
        for j in 0..<list[0].count{
            result[j][list[0].count - i - 1] = list[i][j]
        }
    }
    return result
}
