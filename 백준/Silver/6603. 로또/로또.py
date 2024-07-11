import sys
input = sys.stdin.readline

def dfs(n,s,alst):
#     종료 조건 : 6개 숫자일 때,
    if n == 6:
        ans.append(alst)
        return

# for문으로 넣기.
    for j in range(s,N):
        dfs(n+1, j+1, alst+[lst[j]])

# 1. 입력값 받기.
while True:
    f_lst = list(map(int,input().split()))
    # 입력값이 0일 때 끝내기.
    if f_lst[0] == 0:
        break
    # 인덱스 0번은 N개의 숫자. 그 뒤로 lst.
    N = f_lst[0]
    lst = f_lst[1:]

    ans = []
    dfs(0,0,[])

    for i in ans:
        print(*i)

    # 입력값 마다 띄어서 정답 출력.
    print()


