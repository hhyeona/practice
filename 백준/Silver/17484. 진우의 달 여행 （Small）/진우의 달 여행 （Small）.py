'''
진우의 달 여행)small

완탐 ?/
같은 방향으로 두번 연속 움직일 수 없음 ) 즉, 이전 방향 기록하고 업데이트 해야 함.
방향 (1,-1) (1,0) (1,+1)

dp..?
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
mx = int(sys.maxsize)

dj = [-1,0,1]
def dfs(i,j,di,mx,sm): # index col,row,sum
    if i == n-1:
        return min(mx,sm)
    for k in dj:
        if k!= di:
            ni = i + 1
            nj = j + k
            if 0 <= ni < n and 0 <= nj < m:
                mx = dfs(ni,nj,k,mx,sm + arr[ni][nj])
    return mx

for j in range(m):
    mx = min(mx,dfs(0,j,3,mx,arr[0][j]))

print(mx)