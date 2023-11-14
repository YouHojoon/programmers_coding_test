import kotlin.math.min
class Solution {
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        var correct = 0
        var zeroCnt = 0
        
        var lottosPtr = 0
        var winNumsPtr = 0
        
        lottos.sort()
        win_nums.sort()
        
        while(lottosPtr < lottos.count() && winNumsPtr < win_nums.count()){
            val lhs = lottos[lottosPtr]
            
            if(lhs == 0){
                zeroCnt++
                lottosPtr++
                continue
            }
            
            val rhs = win_nums[winNumsPtr]
            
            when{
                lhs == rhs -> {
                    correct++
                    lottosPtr++
                    winNumsPtr++
                }
                lhs < rhs -> lottosPtr++
                else -> winNumsPtr++
            }
        }
        
        val maxGrade = min(7 - (correct + zeroCnt),6)
        val worstGrade = min(7 - correct,6)
        
        var answer: IntArray = intArrayOf(maxGrade, worstGrade)
        return answer
    }
}
