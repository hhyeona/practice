'''
최대공약수와 최소공배수
'''
a,b = map(int,input().split())
mi = 0
mx = 0
for i in range(min(a,b), 0, -1):
    if a % i == 0 and b % i == 0:
        mi = i
        break

for j in range(max(a,b), (a*b)+1):
    if j % a == 0 and j % b == 0:
        mx = j
        break


print(mi)
print(mx)