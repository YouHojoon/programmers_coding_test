import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var genresPlays = [String:Int]()
    var selectedMusic = [String:[Int]]()
    var result = [Int]()
    
    for (i, (genre, play)) in zip(genres,plays).enumerated(){
        genresPlays[genre] = genresPlays[genre, default: 0] + play
        
        var selectedMusicOfGenre = selectedMusic[genre, default:[]]
        
        if selectedMusicOfGenre.count < 2{
            selectedMusicOfGenre.append(i)
        }
        else{
            let victimIndex = getVictimIndex(selectedMusicOfGenre[0], selectedMusicOfGenre[1], plays)
            let selectedIndex = getVictimIndex(victimIndex, i, plays) == victimIndex ? i : victimIndex
            selectedMusicOfGenre[selectedMusicOfGenre.firstIndex(of:victimIndex)!] = selectedIndex
        }
         selectedMusic[genre] = selectedMusicOfGenre
    }
    
    for item in genresPlays.sorted{$0.1 > $1.1}{
        let genre = item.key
        
        if let selectedMusicOfGenre = selectedMusic[genre]{
            selectedMusicOfGenre
            .sorted{
                if plays[$0] == plays[$1]{
                    return $0 < $1
                }
                return plays[$0] > plays[$1]
            }
            .forEach{result.append($0)}
        }
    }
    
    return result
}

func getVictimIndex(_ lhs: Int, _ rhs: Int, _ plays: [Int]) -> Int{
    let victimIndex: Int
    if plays[lhs] == plays[rhs] {
        victimIndex = lhs > rhs ? lhs : rhs
    }
    else{
        victimIndex = plays[lhs] < plays[rhs] ? lhs : rhs
    }
    return victimIndex
}
