'''
import sys 안쓰면 안됨. 메모리 초과 남.
input = sys.stdin.readline
10,000보다 작거나 같은 자연수!!

일반 버블 정렬
def bubble(arr):
    global N
    for g in range(N-1, 0, -1):
        for k in range(g):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]

N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

bubble(lst)

for j in lst:
    print(j)
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*10001

for i in range(N):
    num = int(input())
    arr[num] += 1 # 그 숫자가 해당하는 위치에 들어온 갯수 카운트

for j in range(10001):
    if arr[j] != 0: # 그 위치에 해당하는 숫자가 존재한다는 것.
        for k in range(arr[j]):  # 그 위치에 해당하는 카운트 만큼 출력.
            print(j)