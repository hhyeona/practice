'''
While문으로 계속 작동하고
멈춰야 할 때만 종료. ( 후진 할 수 없을 때)

4방향 탐색 먼저 수행 -> 빈칸 있으면 이동, 없으면 뒤로 한칸 가서 반복.
뒤로 못 가면 종료.

시간 복잡도 : while문 최대 n * m
각 칸에서 4방향 연산 수행.

청소 x : 0, 벽 :1, 청소 O : 2
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True: #계속 동작.
    if arr[r][c] == 0:
        arr[r][c] = 2 # 청소 시작.
        cnt += 1
    flag = False
    for k in range(1,5): # 90도 회전도 포함하려면 현재 위치에서 -1씩 해주면 됨.(dx,dy)
        nx = r + dx[d-k]
        ny = c + dy[d-k]
        if 0<= nx < n and 0<= ny < m and arr[nx][ny] == 0: # 빈공간.
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진.
            d = (d-k + 4) % 4
            r = nx
            c = ny
            flag = True
            break  # 다시 While문 반복.

    # 4방향 청소할 공간 없는 경우 ( 2 이거나 1이거나)
    if flag == False:
        # 바라보는 방향 유지한 채 후진하고 다시 청소.
        nx = r - dx[d]
        ny = c - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                break
            else:
                r = nx
                c = ny

        else:
            break

print(cnt)