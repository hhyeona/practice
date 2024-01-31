'''
방향 없는 그래프가 주어졌을 때,
연결 요소 (Connected Comonent) 의 개수를 구하는 프로그램.

6 5
1 2
2 5
5 1
3 4
4 6

2
dfs ( 재귀 함수 . 새로운 dfs 들어갈 때 마다 cnt)
큰 구역을 카운팅.

import sys
input = sys.stdin.readline

def dfs(num):
    v[num] = 1  # 방문 노드 추가.
    for j in graph[num]:  # 그래프에 연결된 노드 방문 표시.
        if not v[j]:
            dfs(j)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

cnt = 0
v = [0] * (n + 1)
for i in range(1, n + 1):
    if not v[i]:# 방문 노드 확인 (안하면 dfs함수 작용 총 갯수가 됨)
        dfs(i)
        cnt += 1
print(cnt)
왜 런타임에러인지 모르겠음..
'''
import sys
input = sys.stdin.readline


def bfs(num):
    q = []
    q.append(num)
    v[num] = 1
    while q:
        tm = q.pop()
        for i in graph[tm]:
            if not v[i]:
                v[i] = 1
                q.append(i)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

cnt = 0
v = [0]* (n+1)
for i in range(1,n+1):
    if not v[i]:
        bfs(i)
        cnt += 1
print(cnt)
