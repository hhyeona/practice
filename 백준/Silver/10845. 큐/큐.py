'''
큐

push x : x 넣음.
pop : 가장 앞에 있는 정수를 뺌. [0] 그리고 출력.
     없는 경우 -1

size :  정수의 개수 len(que)
empty : len(que) == 0 이면, 1 or 0
front: 가장 앞 정수 없으면 -1
back: 가장 뒤에 있는 정수 없으면 -1
'''
import sys
input = sys.stdin.readline
n = int(input())

que = []
for i in range(n):
    lst = input().split()

    if lst[0] == 'push':
        que.append(lst[1])

    if lst[0] == 'pop':
        if len(que) != 0:
            print(que.pop(0))
        else:
            print(-1)
    if lst[0] == 'size':
        print(len(que))
    if lst[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    if lst[0] == 'front':
        if len(que) != 0 :
            print(que[0])
        else:
            print(-1)
    if lst[0] == 'back':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)



