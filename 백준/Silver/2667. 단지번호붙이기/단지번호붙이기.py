'''
단지 번호 붙이기
dfs 연습.
'''
import sys
input = sys.stdin.readline

di = [-1,0,1,0]
dj = [0,1,0,-1]
def dfs(i,j,v):
    global count
    count += 1 # 여기서 1을 세어줌.
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if 0<= ni < n and 0<= nj < n and v[ni][nj] != 1 and arr[ni][nj] == 1:
            v[ni][nj] = 1
            dfs(ni,nj,v)



n = int(input())
arr = [list(map(int,input().strip())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
ans = []
count  = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] != 1:
            v[i][j] = 1
            count = 0 # 갱신해줘야함.
            dfs(i,j,v)
            ans.append(count)

ans.sort()
print(len(ans))
for i in ans:
    print(i)

