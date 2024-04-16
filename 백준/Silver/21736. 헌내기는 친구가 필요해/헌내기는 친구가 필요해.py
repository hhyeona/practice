'''
str.
DFS
- 파이썬은 기본 재귀 깊이가 1000으로 매우 얕다.
 따라서 재귀함수를 사용할 시 setrecursionlimit() 함수를 써서 늘려야
 런타임 에러 (RecursionError)가 나지 않는다.
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 제한 늘이기

n,m = map(int,input().split())
arr = [list(map(str,input().strip())) for _ in range(n)]
v = [[0]*m for _ in range(n)]

di = [-1,0,1,0]
dj = [0,1,0,-1]


def dfs(si,sj):
    global cnt
    v[si][sj] = 1
    if arr[si][sj] == 'P':
        cnt += 1

    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0<= ni < n and 0<= nj < m and v[ni][nj] != 1:
            if arr[ni][nj] != 'X':
                dfs(ni,nj)

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            dfs(i,j)

if cnt==0:
    print("TT")
else:
    print(cnt)
