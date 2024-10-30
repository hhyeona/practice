function solution(array, n) {
    array.sort((a,b) => a-b)
    let mi = Infinity;
    let ans = 0;
    for(i of array){      
        let tm = Math.abs(n-i)
        if (tm  < mi){
            mi = tm;
            ans = i
        }
    }
    return ans
}