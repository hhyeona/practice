'''
마인크래프트

땅 고르기
n, n 집터 (0,0)

1. 좌표(i,j)  가장 위에 있는 블록 제거 -> 인벤토리에 추가 : 2초
2. 인벤토리 블록 꺼내서 (i,j) 의 가장 위에 놓음. : 1초

최소 시간, 땅의 높이 출력.(제일 높은 것)

인벤토리 - B 개 블럭 들어있음.
땅의 높이 256 초과 없음. 음수 없음.

N, M , B ( 1<= M,N <= 500, 0 <= B <= 6.4 * 10 ^7)
N 개 줄 M 개의 정수로 땅의 높이 주어짐.

def max_count(arr):
    lst = []
    for i in range(n):
        for j in range(m):
            lst.append(arr[i][j])
    return max(lst, key=lst.count)

시간 초과 남. ( array 에서 빈도 max 찾는 함수)
최대 높이 256. -> 브루트포스

0층 부터 256층 까지 for 문 돌림.
초과 + 인벤토리 블럭수 > 부족분 인경우에만,,!!
걸리는 시간과 층수를 각각 구함.

시간초과 어렵다,,
'''
import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

maxx = 0
sec = sys.maxsize  # 정수 최댓값 할당.

for floor in range(257):
    over, lack = 0, 0
    for k in range(n):
        for j in range(m):
            if arr[k][j] > floor:  # 초과분
                over += (arr[k][j] - floor)
            else:
                lack += (floor - arr[k][j])  # 부족분

    if over + b >= lack: # 초과가 부족보다 많으면 (평평하게 할 수 있음)
        if (over*2) + lack <= sec:
            sec = (over * 2) + lack
            maxx = floor  # 가장 높은 층


print(sec, maxx)