'''
N (1<= N <= 50만)
정수 M 개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는가.

이진탐색으로 하고, 중복 된 값을 count?
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int,input().split())))
m = int(input())
target = list(map(int,input().split()))

count = {}
for a in lst:
    if a in count:
        count[a] += 1
    else:
        count[a] = 1

def bi(lst,targetnum,start,end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if lst[mid] == targetnum:
        # return lst[start:end+1].count(targetnum)
        return count.get(targetnum)
    elif lst[mid] > targetnum:
        return bi(lst,targetnum,start,mid-1)
    else:
        return bi(lst,targetnum,mid+1,end)

ans = []
for i in target:
    start = 0
    end = n-1
    tm = i
    ans.append(bi(lst,tm,start,end))

print(*ans)


