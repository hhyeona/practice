'''
input() 개수를 모를 때, try - except 문 쓰거나 import sys 씀.
'''
while True:
    try:
        a,b = map(int,input().split())
        if a and b != 0:
            print(a+b)
    except:
        break