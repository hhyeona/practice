'''
SWEA 에 국가 국기 문제랑 비슷한 듯?
TIP :  색종이랑 비슷하기도 함.
주어진 목표 구역 만큼을 기준으로 다 훑음.
체스판 처럼 번갈아 가려면 (1,1) 를 (x+y) % 2 == 0  짝수,
(1,2) 는 홀수임.
(2,1) 홀 수 (2,2) 짝수.
그 중에 가장 작은 변화를 답으로 냄.
시작이 B 일 떄, W 일 때로 나누어서 계산함.

'''
# import sys
# input = sys.stdin.readline().strip('\n')
n, m = map(int,input().split())
arr = []
lst = []
for _ in range(n):
    arr.append(input())

for i in range(n-7):
    for j in range(m-7):
        black = 0  # black 으로 시작.
        white = 0  # white 으로 시작.
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'B':
                        black += 1
                    if arr[a][b] != 'W':
                        white += 1
                else:
                    if arr[a][b] != 'W':
                        black += 1
                    if arr[a][b] != 'B':
                        white += 1

        lst.append(black)
        lst.append(white)

print(min(lst))