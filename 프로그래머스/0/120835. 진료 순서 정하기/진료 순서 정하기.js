function solution(emergency) {
//     Slice() 로 깊은 복사 해줌.
    let tm = emergency.slice().sort((a,b) => b-a);
    return emergency.map(v=> tm.indexOf(v) + 1)
}