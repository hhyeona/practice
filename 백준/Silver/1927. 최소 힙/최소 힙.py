'''
the smallest heap.

1. x of number put in the array.
2. print to small number in the array, remove to the number.

N(1 ≤ N ≤ 100,000)

number : add
0 : print to samll numebr and remove.
x <= 2^31

caution.
len(array) == 0: if 0 -> print(0)


## 우선순위를 가진 요소들의 모음
연산
우선순위 큐 (Priority Queue) : O(logN)
insert(x) : 우선순위 큐에 요소 x 추가
remove() : 우선순위 큐에서 가장 우선순위가 높은 요소를 삭제하고 반환
find() : 우선순위 큐에서 가장 우선순위가 높은 요소를 반환

import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    num = int(input().strip())

    if num > 0:
        array.append(num)
    else:
        if len(array) != 0:
            mi = min(array)
            m_index = array.index(mi)
            print(array.pop(m_index))
        else:
            print(0)
time over.
'''
import sys
input = sys.stdin.readline
import heapq # for heap

n = int(input())
heap = []

for _ in range(n):
    num = int(input().strip())

    if num != 0:
        heapq.heappush(heap, num)  # how to use heapq. (list,number)
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap))  # the small number remove.
        else:
            print(0)


