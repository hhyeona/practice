'''
BFS 연습
백준 아기 상어.
bfs = 0(V+E)
V = N * N = 20 * 20
E = V*4
이동 조건 : 작거나 같은 경우
먹기 조건 : 작은 경우 + 가장 가까운 거리, 행 우선, 열 다음.

* 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
이걸 어떻게 처리해야 하는 지는 잘 모르겠음! (행 우선, 열 다음.)
==> 람다로 정렬해줌. 위(행 낮은 순.) 왼쪽(열 낮은 순)
#처음 방식은 틀렸음.-> 9는 위치 일 뿐, 아기 상어 초기 크기 2!!!
전부 다 탐색 해야 함.

'''
import sys
input = sys.stdin.readline
from collections import deque


# bfs (아기 상어에서 시작해서 마름모 모양으로 +1 해서 탐색해 나감.)
# 최단 거리에 먹을 수 있는 값이 있으면 tlst에 좌표 추가 함.
# 거리도 구함.
di = [-1,0,1,0]
dj = [0,1,0,-1]
def bfs(si,sj):
    q = deque()
    v = [[0] * n for _ in range(n)] # 방문 표시
    tlst = [] # 가깝고 작은 물고기 좌표 초기 리스트.
    # 초기 데이터 q 에 삽입.
    q.append((si,sj)) # q에 넣어야지
    v[si][sj] = 1 # 방문 표시.
    dist = 0
    while q:
        ci,cj = q.popleft() #q에서 하나 꺼내.
        # 종료조건 : dist(거리)가 v[ci][cj]면 증가 했다는 것.(그 이전 거리는 다 넣었다는 것)
        # 그러면 종료 하고 tlst에 있는 걸로 계산하고 와야지.
        if dist == v[ci][cj]:
            return tlst, dist-1
        #4방향 , 범위내, 미방문, 조건(나보다 작거나 같으면 지나갈 수 있음)
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<= ni < n and 0<= nj < n and v[ni][nj] == 0 and arr[ni][nj] <= shark:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1 # 거리 늘려서 추가.
                # 나보다 작은 물고기면 tlst에 드디어 추가.
                if shark > arr[ni][nj] > 0:
                    tlst.append((ni,nj))
                    dist = v[ni][nj] # 그만큼 거리 갱신.

    return tlst,dist-1

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

shark = 2  # 초기 아기 상어 크기 2.
eat_cnt = ans = 0  # cnt  : 상어 크기 만큼 먹으면 사이즈 +1 할 수 있음.
# ans : 먹으려고 이동한 거리 누적.

# 아기 상어 좌표 구함.
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            ci, cj = i, j
            arr[i][j] = 0 # 아기 상어 자리 0으로 초기화 (지나가야 함)

# bfs 에서 구한 tlst(좌표)와 dist(거리)값을 가지고 먹으면서 사이즈 갱신.
# 최종 거리도 구해서 답을 냄.
while True: # 무한 루프 (tlst 값이 나올 때까지 해야 하니까)
    tlst, dist = bfs(ci,cj)
    if len(tlst) == 0: # 탐색할 리스트가 없으면 끝이지.
        break
    # 조건대로 위부터 그 다음 왼쪽부터 (행/열 정렬)
    tlst.sort(key=lambda x:(x[0],x[1]))
    ci,cj = tlst[0]  # 가장 가깝고 먹을 수 있는 좌표 꺼냄.
    arr[ci][cj] = 0 # 먹었으니까 0
    eat_cnt += 1 # 한번 먹었다.
    ans += dist
    if shark == eat_cnt: # 현재 상어 크기 만큼 cnt가 같으면
        shark += 1  #상어 크기 +1
        eat_cnt = 0    # 먹은 수 다시 초기화.

print(ans)