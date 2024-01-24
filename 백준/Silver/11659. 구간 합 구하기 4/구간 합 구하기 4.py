'''
구간합 구하기 4

수 n개가 주어졌을 때,
i 번째 수부터 j 번째 수까지 합을 구함.

수의 개수 n, 합을 구해야 하는 횟수 m (i~j)

n,m <= 천.
1 <= i <= j <= n

나와 있는 걸 일일이 더해도 되지만,
왠지 DP 이용해서 index 증가할 때마다 더해 놓고,
나중에 구간 아닌 부분까지 빼도 될 듯?

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))
for _ in range(m):
    i,j = map(int,input().split())
    cnt = sum(lst[i-1:j])  # index는 0이지만, 숫자는 1부터임.
    print(cnt)

역시나 시간초과..싸우자!
'''
import sys
input = sys.stdin.readline

n , m = map(int,input().split())
lst = list(map(int,input().split()))
dp = [0] * (n+1)

for g in range(1,n+1):
    dp[g] = dp[g-1] + lst[g-1]

for _ in range(m):
    i, j = map(int,input().split())

    ans = dp[j]-dp[i-1]
    print(ans)

