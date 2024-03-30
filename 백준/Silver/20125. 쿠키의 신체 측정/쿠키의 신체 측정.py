import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(str,input().strip())) for _ in range(n)]
heart = []
flag = False

for i in range(n):
    for j in range(n):
        if arr[i][j] =='*':
            heart.append(i+2)
            heart.append(j+1)
            flag = True
            break
    if flag == True:
        break

print(*heart)
x = heart[0]
y = heart[1]

# 왼팔 / 오른팔
l_arm = arr[x-1][:y-1].count('*')
r_arm = arr[x-1][y:].count('*')
# 몸통
center = fin = 0
for i in range(x,n):
    if arr[i][y-1] == '*':
        center += 1
    else:
        fin = i-1
        break
# 왼다리/오른다리
l_leg = 0
for i in range(fin+1,n):
    if arr[i][y-2] == '*':
        l_leg += 1

r_leg = 0
for i in range(fin+1,n):
    if arr[i][y] == '*':
        r_leg += 1


print(l_arm,r_arm,center,l_leg,r_leg)