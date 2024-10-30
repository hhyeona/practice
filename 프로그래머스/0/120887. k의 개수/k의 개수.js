function solution(i, j, k) {
    let tm = ''
    for(let g=i; g <= j; g++){
        tm += g
    }
    return tm.split(k).length-1
}