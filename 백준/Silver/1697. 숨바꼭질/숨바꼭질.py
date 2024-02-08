'''
N(0 ≤ N ≤ 100,000)

K(0 ≤ K ≤ 100,000)

X 위치.  X + 1 , -1
        X * 2

세가지 연산으로 가장 빠르게 k 에 도달.
5 17

5-10-9-18-17 : 4초 만에 도달 가능.
BFS 로 풀면 됨. ( 이유 : 3가지 방법으로 가지쳐서 계속 번져감)
'''
from collections import deque
N, K = map(int,input().split())
mx = 10**5   # 시간 초과 안나도록 수 제한.
v = [0] * (mx+1)
def bfs():
    q = deque()
    q.append(N) # q = deque([5])
    while q:
        i = q.popleft() # 처음 i = 5, q = deque([])
        if i == K: # 원하던 값이면 cnt 출력하고 종료.
            print(v[i])   #
            break
        for ni in (i-1,i+1,i*2):  # 4, 6, 10
            if 0 <= ni <= mx and not v[ni]:
                v[ni] = v[i] + 1   # 간선 가짓수 늘리기.
                q.append(ni)

bfs()
