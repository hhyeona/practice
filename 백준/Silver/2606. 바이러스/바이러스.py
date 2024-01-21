'''
바이러스
바이러스에 걸리게 되는 컴퓨터의 수 출력.
컴퓨터 수 100이하.
노트(간선의수) 주어짐.
연결되어있는 컴퓨터 번호의 쌍이 주어짐.
7
6
1 2
2 3
1 5
5 2
5 6
4 7
1번이 걸렸을 때, 1번을 통해 감염되는 컴퓨터의 총 수 출력.
4

DFS로 품.
깊이 우선 탐색.
'''
import sys
input = sys.stdin.readline

node = int(input())
line = int(input())
graph = [[] for i in range(node+1)]  # 그래프 초기화 (인접 리스트 만들 것임)
visited = [0]*(node+1)               # 방문 표시 따로.

def dfs(line):              # 그래프 끼리 연결된 부분 방문 표시 하나씩 해줌.
    visited[line] = 1
    for nx in graph[line]:   # 현재 노드와 연결 된 다른 노드를 재귀적으로 방문.
        if visited[nx] == 0:
            dfs(nx)

for i in range(line):
    a,b = map(int,input().split())   # 입력값들을 서로 연결시켜줌.(리스트로 변환)
    graph[a] += [b]
    graph[b] += [a]

dfs(1) # 1과 연결 된 점.
print(sum(visited)-1) # 1번 컴퓨터 제외.