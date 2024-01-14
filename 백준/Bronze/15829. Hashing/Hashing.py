'''
Hashing
r = 31
M = 1234567891
'''
L = int(input())
st = input()
alpha = 'zabcdefghijklmnopqrstuvwxyz'
al_list = list(str(alpha))
st_list = []
ans = 0
for j in range(L):
    for i in range(1,27):
        if st[j] == al_list[i]:
            st_list.append(i)

for k in range(L):
    ans += st_list[k] * (31**k)

print(ans)

