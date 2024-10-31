function solution(n) {
    let tm = 0
    for (let _=0; _<n; _++){
        tm += 1
        while(tm % 3 ==0 || tm.toString().split('').includes('3')){
            tm += 1
        }
    }
    return tm
}