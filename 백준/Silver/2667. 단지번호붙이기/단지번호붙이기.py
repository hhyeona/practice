import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().strip())) for _ in range(n)]
ans = []
v = [[0] * n for _ in range(n)]
di = [-1,0,1,0]
dj = [0,1,0,-1]

def dfs(i,j,v):
    global cnt
    cnt += 1

    for k in range(4):
        ni,nj = i + di[k], j + dj[k] 
        if 0<= ni < n and 0<= nj < n and v[ni][nj] == 0 and arr[ni][nj] == 1:
            v[ni][nj] = 1
            dfs(ni,nj,v)
    
    return cnt

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] ==0:
            cnt = 0
            v[i][j] = 1
            ans.append(dfs(i,j,v))
            
            
ans.sort()
print(len(ans))
for i in ans:
    print(i)