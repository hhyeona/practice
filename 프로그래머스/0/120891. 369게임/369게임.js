function solution(order) {
//     nullish 연산자 null 또는 undefined일때, 오른쪽 아니라면 왼쪽.
    // let value = order.toString().match(/[369]/g) ?? []
    // return value.length;
    
//     filter 
    // return order.toString().split('').filter(v=>v==='3'|| v==='6'||v==='9' ? true : false).length
//     Set
    const s = new Set('369')
    return order.toString().split('').filter(v=>s.has(v)).length
}