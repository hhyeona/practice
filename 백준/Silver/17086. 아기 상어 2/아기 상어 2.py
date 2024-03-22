'''
안전 칸 -> 그 칸과 가장 거리가 가가운 아기 상어와의 거리.
8방향.
ans = 안전 거리가 가장 큰 칸.
'''
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

di = [-1,-1,-1,0,1,1,1,0]
dj = [-1,0,1,1,1,0,-1,-1]
def bfs(i,j):
    cnt = 0
    v = [[0]*m for _ in range(n)]
    q = deque()
    v[i][j] = 1
    q.append((i,j))
    while q:
        ci,cj = q.popleft()
        # 종료 조건 : 현재 arr값이 1이라면 v배열에 넣었던 cnt값에서 -1 (초기를 1로 해서 -1 해줌)
        if arr[ci][cj] == 1:
            cnt = v[ci][cj] - 1
            return cnt
        for k in range(8):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<= ni < n and 0<= nj < m and v[ni][nj] == 0 :
                v[ni][nj] = v[ci][cj]+1
                q.append((ni,nj))

    return cnt

tlst = []
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            tm = bfs(i,j)
            tlst.append(tm)

ans = max(tlst)
print(ans)