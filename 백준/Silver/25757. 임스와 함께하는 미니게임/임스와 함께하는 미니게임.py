'''
Y = 2
F = 3
O = 4

N = 십만.
'''
import sys
input = sys.stdin.readline

n , game = map(str,input().split())
N = int(n)
lst = []
for _ in range(N):
    name = input().strip()
    lst.append(name)

set_lst = set(lst) # 중복 제거.
dic = {'Y':1,'F':2,'O':3} # 게임 인원 선택
real = len(set_lst)
num = dic[game]

ans = real // num
print(ans)

