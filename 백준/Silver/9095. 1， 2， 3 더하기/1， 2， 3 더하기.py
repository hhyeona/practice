'''
1,2,3 더하기

정수 4를 1,2,3 의 합으로 나타내는 방법은 총 7가지 있음.

n < 11.
방법의 수 출력.

DP 이용.
dp[1] = 1
dp[2] = 1+1, 2 : 2
dp[3] = 1+1+1, 1+2, 2+1, 3: 4
dp[4] = 1+1+1+1, 1+2+1, 2+1+1, 1+1+2, 2+2, 1+3, 3+1 : 7
dp[5] = 1+1+1+1+1, 1+1+1+2(4개), 2+2+1(3개), 1+1+3(3개), 3+2,2+3 :13개

5를 구할 때, 2에서 +3을 하면 5.
3에서 +2. 4에서 +1 을 하면 됨.
따라서 DP(N) = dp(n-3) + dp(n-2) + dp(n-1)을 하면 됨.

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = int(input())

    dp = [0]*(num+1)

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if num >= 4:
        for i in range(4,num+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[num])
런타임 에러 나옴.
'''
import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 12  # n < 11 이니까. (index 에 맞춰서 12개) 초기화.
for _ in range(T):
    num = int(input())

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for n in range(4,11):
        dp[n] = dp[n-3] + dp[n-2] + dp[n-1]

    print(dp[num])
