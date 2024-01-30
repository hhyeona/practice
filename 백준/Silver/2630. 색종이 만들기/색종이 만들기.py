'''
N 한 변 길이.
N 은 2,4,8,16,32,64,128 중 하나임.
하얀색 0
파란색 1

하얀색 종이 개수
파란색 종이 개수 출력.

분할 정복 / 재귀함수


'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
blue = 0
white = 0

def color(i,j,n):
    global white,blue
    col = arr[i][j]
    for k in range(i,i+n):
        for g in range(j,j+n):
            if col != arr[k][g]:
                color(i,j,n//2)
                color(i,j+n//2,n//2)
                color(i+n//2,j,n//2)
                color(i+n//2,j+n//2,n//2)
                return
    if col == 0:
        white += 1
    else:
        blue += 1


color(0,0,n)
print(white)
print(blue)

