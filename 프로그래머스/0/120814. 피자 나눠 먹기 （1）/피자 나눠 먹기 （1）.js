function solution(n) {
    var answer = 0;
    if(n/7 == ~~(n/7)){
       answer = ~~(n / 7)
       } else {
        answer = ~~(n/7) +1
    }
    return answer;
}