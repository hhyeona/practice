import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * (n+1)
lst = [0]
for _ in range(n):
    num = int(input())
    lst.append(num)

for i in range(1,n+1):
    for j in range(1,i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
