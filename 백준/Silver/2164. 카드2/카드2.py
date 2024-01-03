'''
N 장의 카드 앞에 하나 버리고 다음 하나 뒤로 쌓고
하나 버리고 다음 하나 쌓고 반복.   => deque 를 사용하기도 함.
from collections imort deque
que = deque()
for i in range(N):
    que.append(i+1)

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que.pop())

1234
234
342
42
24
4

123456
23456
34562
4562
5624
624
모든 홀수가 사라지고 짝수 순서가 됨.
246
46
64
4

12345
2345
3452
452
524
24
4

2468
468
684
짝수 애들만 남음.
84
48
8

246810
46810
68104
8104
1048
결국은 또 짝수애들만 남음.
48
84
4

2 4 6 8 10 12 14
68101214 4
101214 4 8
14 4 8 12
짝수 애들만 남음.
8 12 4
12 4
4 12
12

n = int(input())
lst = []

for i in range(1, n+1):
    lst.append(i)

cnt = 0
ans = 0
while len(lst) >= 0:
    if len(lst) > 1:
        if cnt % 2 == 0:
            lst.pop(0)
            cnt += 1

        elif cnt % 2 != 0:
            lst.append(lst.pop(0))
            cnt += 1

    elif len(lst) == 1:
        ans = lst[0]
        break

print(ans)

위에 답 시간 초과.
정수 50만개. O log(N) 이 필요할 듯?.
짝수로만 해도 시간초과.
n = int(input())
lst = []

for i in range(1, n+1): # 짝수만 리스트 넣음.(홀수는 어차피 삭제됨)
    if i % 2 == 0:
        lst.append(i)

cnt = 0
ans = 0
while len(lst)> 0:
    if len(lst) > 1:
        if cnt % 2 == 0:
            lst.pop(0)
            cnt += 1
        else:
            lst.append(lst.pop(0))
            print(lst)
            cnt += 1

    elif len(lst) == 1:
        ans = lst[0]
        break

print(ans)

규칙.
6 : 2^2
8 : 2^3
10 : 2^2

(10-8)*2
(N-2^(N의 결과보다 한단계 작은 2의 제곱)) * 2  <- 넘어갈 때, 작게 하면 됨.

1 <= N <= 50만
'''
import sys
input = sys.stdin.readline()

n = int(input)
ans = 0

square = 2
while True:
    if n == 1 or n == 2:
        ans = n
        break
    square *= 2

    if square >= n:
        ans = (n-(square//2)) * 2
        break

print(ans)

