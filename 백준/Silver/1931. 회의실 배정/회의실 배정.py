'''
한 개 회의실.
시작 - 끝

최대한 많은 회의 몇 개?

그리디(현재 가장 좋은 것부터 선택) / 정렬.

'''
import sys
input = sys.stdin.readline

lst = []
n = int(input())
for _ in range(n):
    s,e = map(int,input().split())
    lst.append([s,e])

lst.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간이 작은 것부터 그 중에 시작도 작은 것.

cnt = present = 0
for start, end in lst:
    if present <= start:   # 현재 빈 회의 부터 시작.
        cnt += 1
        present = end     # 회의 끝난 시간으로 갱신.

print(cnt)
