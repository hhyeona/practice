function solution(s) {
    s = s.split(' ')
    let result = []
    for (let i of s){
        if(i==='Z'){
            result.pop()
        }else {
//             + 숫자로 변환.
            result.push(+i)
        }
    }
    return result.reduce((a,c) => a+c, 0)
}