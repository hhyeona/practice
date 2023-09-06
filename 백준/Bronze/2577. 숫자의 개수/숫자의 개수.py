'''
숫자를 각 리스트로 저장하는게 관건. 
list(map(int,str(?))) 하면 각 자릿수를 리스트로 나눠서 저장 가능.
'''
A = int(input())
B = int(input())
C = int(input())

ans = (A*B*C)
lans = list(map(int,str(ans)))

lst = [0]*10

for i in lans:
    lst[i] += 1

for j in lst:
    print(j)