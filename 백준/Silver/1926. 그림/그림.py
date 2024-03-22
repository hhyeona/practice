'''
BFS 연습.
from collections import deque
1. 아이디어
  - 2중 for => 값 1 && 방문 x => bfs
  - BFS 돌면서 그림 개수 + 1, 최대값을 갱신.
2. 시간복잡도
BFS = 0(V*E) =  5V = 500 * 500 * 5 < 2억개 ( 1초)
V = m * n (노드)
E = V * 4 (간선)
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- queue(bfs)
'''
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
v = [[False] * m for _ in range(n)]
cnt = mx = 0 #cnt 그림 개별로 구하고/ 그림의 최댓값 갱신 위해 변수 할당

dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 첫 1을 발견하면 bfs로 연결된 그림들 갯수 세어줌.
def bfs(x,y):
    rs = 1 # 초기 그림의 cnt 할당. 1로 들어온 거니까 당연히 1부터 시작.
    q = [(x,y)] # 초기 좌표 할당.
    while q: # q 가 비어있지 않을 때까지.
        di,dj = q.pop()
        for r in range(4): # 사방으로 1 찾음.
            ni = di + dx[r]
            nj = dj + dy[r]
            if 0<= ni < n and 0<= nj < m :  # next 조건.
                if arr[ni][nj] == 1 and v[ni][nj] == False: # 그림 넓힐 때 조건.
                    rs += 1    # next가 1이면 그림 범위 추가해주고.
                    v[ni][nj] = True   # 방문 표시로 다음에 다시 오지 않게 해주고.
                    q.append([ni,nj])  # q 에 넣어서 넓혀가야지.
    return rs  # 넓이를 리턴.



# 1을 마주하면 방문한 적이 없는지 보고 BFS 돌려서 갯수 구함.
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and v[i][j] == False:
            v[i][j] = True  # 반드시 방문 표시!!
            cnt += 1   # 그림의 첫 1이니까.
            mx = max(mx, bfs(i,j))

print(cnt)
print(mx)


