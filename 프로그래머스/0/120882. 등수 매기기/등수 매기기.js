function solution(score) {
    let tm = []
    for (let i =0; i<score.length; i++){
        tm.push((score[i][0] + score[i][1]) / 2)
    }
    let result = tm.slice().sort((a,b) => b-a)
    return tm.map((v) => result.indexOf(v) + 1);
}