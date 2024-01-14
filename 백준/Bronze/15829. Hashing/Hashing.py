'''
Hashing
r = 31
M = 1234567891
--
a 아스키코드 97 이라서 -96 해주면 1 로 할당가능.
alphabe * r ^ i Mod M
'''
M = 1234567891
r = 31

L = int(input())
al = input()

ans = 0
for i in range(len(al)):
    num = ord(al[i]) - 96
    ans += num * (r**i)

print(ans %  M)


