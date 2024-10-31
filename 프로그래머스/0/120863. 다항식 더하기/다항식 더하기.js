function solution(polynomial) {
    const tm = polynomial.split(' + ')
    const x_ans = tm.filter(v => v.includes('x')).map((v) => parseInt(v.replace('x','')) || 1).reduce((a,c) => a+c,0)
    const n = tm.filter(v=> !v.includes('x')).reduce((a,c) => a+parseInt(c),0)
    let answer = []
    if(x_ans){
        if(x_ans===1){
            answer.push('x')
        } else {
            answer.push(`${x_ans}x`)
        }
    }
     if (n){
        answer.push(n)
    }
    return answer.join(' + ')
}