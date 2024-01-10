'''
팰린드롬수
0 은 앞에 올 수 없음.
1 이상 99999 이하의 정수가 주어짐.
마지막 줄에는 0이 포함.
'''
#import sys
#input = sys.stdin.readline

while True:
    lst = input()
    if lst == '0':
        break

    if lst == lst[::-1]:  # 역순과 같으면
        print('yes')
    else:
        print('no')