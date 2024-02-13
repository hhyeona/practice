'''
쉬운 최단 거리.

n, m 이 주어짐.
0 갈 수 없는 땅. 1은 갈 수 있는 땅. 2 목표.

각 지점에서 목표지점까지 거리 출력. 도달 할 수 없으면 -1 출력.

BFS 거리탐색.
'''
import sys
input = sys.stdin.readline
from collections import deque  #for bfs

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]  # 방문 못하면 -1 출력.

di, dj = [-1,0,1,0], [0,1,0,-1]  # 가로, 세로 이동

def bfs(i,j):
    que = deque()
    que.append((i,j))

    visited[i][j] = 0

    while que:
        x,y = que.popleft()

        for g in range(4):
            ni, nj = di[g]+x, dj[g]+y

            if 0<= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
                if arr[ni][nj] == 0:  # 갈 수 없음.
                    visited[ni][nj] = 0
                if arr[ni][nj] == 1:  # 갈 수 있으면
                    visited[ni][nj] = visited[x][y] + 1  # 그 전꺼에서 +1
                    que.append((ni,nj))  # 그 다음 타자.

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:   # 방문을 못했을 때,
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')

    print()  # 원하는 포맷이 나옴.


        