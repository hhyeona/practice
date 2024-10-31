function solution(board) {
    const n = board.length
    const d =[
        [0,0],
        [0,1],
        [0,-1],
        [1,1],
        [1,0],
        [1,-1],
        [-1,-1],
        [-1,0],
        [-1,1]        
    ]
    let dangerZone = new Set()
    for (let i = 0; i<n; i++){
        for (let j = 0; j<n; j++){
            if(board[i][j] == 1)
                d.forEach((v)=>{
                    let [x,y] = [i+v[0],j+v[1]]
                    if (x >= 0 && x < n && y >= 0 && y < n){
                        dangerZone.add(x + " "+ y)
                    }
                })
        }
    }
    return n*n-dangerZone.size;
}