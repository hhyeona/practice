'''
DFS and BFS

point.
Nodes with fewer numbers should be visited first.
AND It terminates when there are no more nodes to visit.

node is n (1 <= n <= 1,000)
line is m (1 <= m <= 10,000)
start to quest is v

'''
import sys
from collections import deque  #for bfs
input = sys.stdin.readline

n,m,f = map(int,input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    start, end = map(int,input().split())
    graph[start][end] = 1
    graph[end][start] = 1

v1 = [0] * (n+1) # dfs visited record
v2 = [0] * (n+1) # bfs visited record

def dfs(i):
    v1[i] = True
    print(i, end=' ')
    for j in range(1,n+1):
        if not v1[j] and graph[i][j]: #if u not visited i value, connected to node i.
            dfs(j)

def bfs(i):
    que = deque([i])
    v2[i] = True
    while que:
        i = que.popleft()
        print(i, end=' ')
        for j in range(1,n+1) :
            if not v2[j] and graph[i][j]:
                que.append(j)
                v2[j] = True

dfs(f)
print()
bfs(f)