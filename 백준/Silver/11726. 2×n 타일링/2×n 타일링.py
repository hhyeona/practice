'''
2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수.

1 <= n <= 천.

첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지 출력.

DP 이용.
dp[1] = 1 가지.
dp[2] = 2 가지.
dp[3] = 3 가지.
dp[4] = 5 가지.
dp[5] = 8 가지.

dp[n] = dp[n-2] + dp[n-1]

# for 문을 n+1 로 하면 런타임에러남.
'''
n = int(input())

dp = [0] * (1001)
dp[1] = 1
dp[2] = 2
dp[3] = 3
ans = 0
if n > 3:
    for i in range(4, 1001):
        dp[i] = (dp[i-2] + dp[i-1])

ans = dp[n] % 10007
print(ans)

