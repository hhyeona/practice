'''
스도쿠
# 기존에 날 것으로 푼건 조건문이 너무 많이 반복 됐음.
이번 풀이는 그걸 보완.
'''
def sudoku(arr):  # for문 한번으로 조건 확인
    # 가로 / 세로
    for i in range(9): # 0 번
        row = [0] * 10
        col = [0] * 10
        for j in range(9): # 0 ~ 8 번
            r = arr[i][j]
            c = arr[j][i]

            if row[r]: return 0 # 이미 있어서 1 이상이면 return 0 이미 끝.
            if col[c]: return 0

            row[r] = 1 # 0 이었으면 + 1
            col[c] = 1
            # 3 * 3 칸 마다
            if i % 3 == 0 and j % 3 == 0:
                nine = [0] * 10
                for k in range(i, i+3):
                    for g in range(j, j+3):
                        num = arr[k][g]
                        if nine[num]: return 0
                        nine[num] = 1
    return 1

t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int,input().split())) for _ in range(9)]

    ans = sudoku(arr)

    print(f'#{tc}', ans)