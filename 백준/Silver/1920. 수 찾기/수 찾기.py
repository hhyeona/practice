'''
수 찾기.
n = int(input())
lst = list(map(int,input().split()))
m = int(input())
target = list(map(int,input().split()))

ans = []
for i in target:
    if i in lst:
        ans.append(1)
    else:
        ans.append(0)

for i in ans:
    print(i)

위 코드 시간초과 됨. 시간 복잡도 : O(N)

모든 정수의 범위 -2^31 <= A < 2^31

자연수 n,m 은 10만개이하.

이분탐색. 으로 시간을 줄임. 시간 복잡도 :  O(logN)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(map(int, input().split()))

m = int(input())
target = map(int, input().split())


def bi(array, ta, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if array[mid] == ta:
        return 1
    elif array[mid] < ta:
        return bi(array, ta, mid + 1, end)
    else:
        return bi(array, ta, start, mid - 1)


for i in target:
    start = 0
    end = n - 1
    print(bi(lst, i, start, end))
