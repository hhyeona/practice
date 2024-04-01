'''
수열 오름차순. (중복 제거 1,2 2,1 안됨. 조합)

첫번째 숫자보다 작은 숫자는 더 이상 추가 안하면 됨.
sort(필요 없음)
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = []

def back(num):
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return

    for i in range(num,n+1):
        if i not in ans:
            ans.append(i)
            back(i+1)  # 갔다가 3이면 그제서야 밑의 pop을 하게 됨.
            ans.pop()


back(1) # 숫자를 늘려줌.(여기서 num은 cnt가 아니라 해당 숫자)