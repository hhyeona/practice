'''
백트래킹 문제. <= N 이 10 언저리로 작음. / 재귀 함수 종료 시점 잊지 말기!!
for문으로 반복 하기 어려움.
재귀 함수로 트리를 번갈아감.(백 트래킹)
3 개 중 2개 순열.
[1,2] 가 들어가고 2를 빼주면서 3을 추가하는 작업 필요.(방문 표시도 리셋)

조건 만족 길이가 M 인 수열 모두 구함.
중복 없이 M개 고름. <= 순열. (순서 중요)
방문 여부 확인.

시간 복잡도
중복 가능하면 n^n  n=8 까지 가능.
중복 불가하면 n!   n=10 까지 가능.
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = []
chek = [False] * (n+1)

def back(num): # num 이 count가 되고.
    if num == m:
        print(' '.join(map(str,ans))) # string으로 변환후 join해서 map으로 프린트
        return
    for i in range(1,n+1):  # 노드를 하나씩 추가해주는 셈이 됨.
        if chek[i] == False:
            chek[i] = True
            ans.append(i)
            back(num+1)
            chek[i] = False
            ans.pop()
back(0)