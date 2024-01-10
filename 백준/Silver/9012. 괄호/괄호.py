'''
괄호

문자열 길이는 2 이상 50 이하.
올바른 문자열 인지 확인.
'''
import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
    lst = list(map(str, input().rstrip()))
    long = len(lst)
    stack = []
    last = []
    cnt = 0
    ans = ''
    for j in range(len(lst)):
        cnt += 1
        if lst[j] == '(':
            stack.append(lst[j])

        if lst[j] == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                ans = 'NO'
                break

    if ans != 'NO':
        if cnt == long and len(stack) == 0:
            print('YES')
        elif cnt == long and len(stack) != 0:
            print('NO')
    else:
        print('NO')