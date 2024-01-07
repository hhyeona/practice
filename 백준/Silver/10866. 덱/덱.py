'''
덱

deque

push_front x : 정수 x를 덱의 앞에 넣음.
push_back x : 정수 x 를 덱의 뒤에 넣음.

pop_front : deque[0] 빼고, 그 수 출력. 만약 없으면 -1
pop_back  : deque[-1] 빼고, 그 수 출력. 없으면 -1

size : len(deque)
empty : 비어있으면 1, 아니면 0

front: deque[0] 출력. 없으면 -1
back: deque[-1] 출력. 없으면 -1

'''
import sys
input = sys.stdin.readline

n = int(input())
deque = []

for i in range(n):
    lst = input().split()

    if lst[0] == 'push_back':
        deque.append(lst[1])
    if lst[0] == 'push_front':
        deque.insert(0, lst[1])
    if lst[0] == 'pop_back':
        if len(deque) != 0:
            print(deque.pop(-1))
        else:
            print(-1)
    if lst[0] == 'pop_front':
        if len(deque) != 0:
            print(deque.pop(0))
        else:
            print(-1)
    if lst[0] == 'size':
        print(len(deque))
    if lst[0] == 'empty':
        if len(deque) == 0 :
            print(1)
        else:
            print(0)
    if lst[0] == 'back':
        if len(deque) != 0 :
            print(deque[-1])
        else:
            print(-1)
    if lst[0] == 'front':
        if len(deque) != 0 :
            print(deque[0])
        else:
            print(-1)