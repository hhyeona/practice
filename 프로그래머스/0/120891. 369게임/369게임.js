function solution(order) {
//     nullish 연산자 null 또는 undefined일때, 오른쪽 아니라면 왼쪽.
    let value = order.toString().match(/[369]/g) ?? []
    return value.length;
}