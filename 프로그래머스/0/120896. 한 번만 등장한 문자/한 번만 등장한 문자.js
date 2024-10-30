function solution(s) {
    return [...s].filter(a => s.split(a).length === 2).sort().join('')
}