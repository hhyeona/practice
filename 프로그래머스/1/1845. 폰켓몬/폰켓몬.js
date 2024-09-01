function solution(nums) {
    var answer = 0;
    N = nums.length / 2
    sett = new Set(nums)
    num_sett = sett.size
    
    if (num_sett < N ){
        answer = num_sett
    } else {
        answer = N
    }
   
       
    return answer;
}