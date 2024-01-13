'''
1 <= N <= 백만개.

'''

import sys
input = sys.stdin.readline


n = int(input())
lst = []
for i in range(n):
    lst.append(int(input().rstrip()))

lst.sort()

for j in lst:
    print(j)