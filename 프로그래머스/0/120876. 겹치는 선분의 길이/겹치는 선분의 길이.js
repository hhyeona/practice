function solution(lines) {
    let line = new Array(200).fill(0)
    lines.forEach(([s,e]) => {
        for (; s < e; s++){
            line[s+100]++
        }
    })
    return line.filter((v) => v>1).length
}