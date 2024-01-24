'''
파도반 수열.

첫 삼각형 1.
계속 추가하다가 가장 긴 변의 길이를 k라 할 때,
k인 정삼각형 추가.

p(10) = 1,1,1,2,2,3,4,5,7

n 은 100이하.
시간 줄이기 위해서는 100까지 다 구해놓고, 찾는 게 빠름.

DP 이용.
규칙을 찾아라.
DP[n] = DP[N-2] + DP[N-3]

import sys
input = sys.stdin.readline

dp = [0] * 100
dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, 100):
    dp[i] = dp[i - 3] + dp[i - 2]

T = int(input())
for _ in range(T):
    target = int(input())
    print(dp[target])
    
런타임..ㅠㅜ
'''
import sys
input = sys.stdin.readline

dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1
for i in range(4, 101): # 101까지 해줘야지!!
    dp[i] = dp[i-3] + dp[i-2]

T = int(input())
for _ in range(T):
    target = int(input().strip())
    print(dp[target])
