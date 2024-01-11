'''
통계학.
N 개의 수를 대표 하는 기본 통계값.

산술평균 : N 개의 수들의 합을 N으로 나눈 값.
중앙값 : N 개의 수들을 증가하는 순서대로 나열 - 그 중앙 위치 값
최빈값 :  N 개의 수들 중 가장 빈도가 많은 값
범위 : N 개의 수들 중 최댓값과 최솟값의 차이.

N  = 50만 이하. (단 홀수임) / N 개의 줄에 정수들 주어짐. (정수는 4000을 넘지 않음)
'''
import sys
input = sys.stdin.readline
n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst.sort()

print(round(sum(lst)/n)) # 산술평균
print(lst[n//2])  # 중앙값

# 최빈값 딕셔너리로 사용. 빈도수 구함.
many =dict()
for i in lst:
    if i in many:
        many[i] += 1
    else:
        many[i] = 1

mx= max(many.values()) # 빈도수 중 최대값
max_num = []

for j in many:
    if mx == many[j]: # 해당 빈도수 키값
        max_num.append(j)

if len(max_num) >1:
    print(max_num[1])
else:
    print(max_num[0])  # 하나면 해당 값 출력.

print(max(lst)-min(lst))  # 범위