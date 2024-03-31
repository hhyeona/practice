'''
촌수계산
'''
import sys
input = sys.stdin.readline

n = int(input())
A, B = map(int,input().split())
line = int(input())
family = [[]*n for _ in range(n+1)] # 0은 없는 넘버라서 +1 해줌.
v = [0] * (n+1)
cnt = 0
flag = 0
def dfs(target,cnt):
    global flag
    v[target] = 1
    if target == B:
        flag = 1
        print(cnt)
    for tm in family[target]:
        if v[tm] == 0:
            dfs(tm,cnt+1)

for _ in range(line):
    a,b = map(int,input().split())
    family[a].append(b)
    family[b].append(a)

dfs(A,cnt)
if flag == 0:
    print(-1)

