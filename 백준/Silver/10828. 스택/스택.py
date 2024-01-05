'''
스택

push X : 정수 X를 스택에 넣는 연산.
pop :  스택에서 가장 위에 있는 정수를 빼고, 그 수 출력. 없는 경우 -1
size : 스택에 들어있는 정수 개수 출력
empty :  스택이 비어 있으면 1, or 0
top :  스택의 가장 위에 있는 정수 출력. 없는 경우 -1 출력.
'''
import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    lst = input().split()

    if lst[0] == 'push':
        stack.append(lst[1])

    elif lst[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop(-1))
        else:
            print(-1)

    elif lst[0] == 'size':
        print(len(stack))

    elif lst[0] == 'empty':
        if len(stack) == 0 :
            print(1)
        else:
            print(0)

    elif lst[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
