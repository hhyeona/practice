'''
계단 오르기 규칙.

1. 한번에 한 계단 or 두 계단씩 오를 수 있음.
2. 연속된 세개의 계단을 모두 밟을 순 없음. 시작점은 포함되지 않음.
3. 마지막 도착 계단은 반드시 밟아야 함.

이때, 계단에 쓰여있는 점수로 얻을 수 있는 최댓값 출력.

계단 수 300이하. (점수는 만점이하 자연수)

전형적인 점화식을 찾는 DP.
도착지부터 생각하는 방식의 접근.

dp[n] = n 번째 올랐을 때 얻을 수 있는 점수의 최댓값.
n-1 번째 계단에서 오는 경우,
: DP(n-3) + stair[n-1] + stair[n]
n-2 번째 계단에서 오는 경우.
: DP(n-2) + stair[n]

1,2,3 층은 초기화 해줘야 함. (n-3 이 있으므로)
'''
import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * 301 # 계단 수 300이하, 초기화.

for i in range(1,n+1):
    stair[i] = int(input())  # 계단 점수 index에 저장.

dp = [0] * 301 # dp 초기화

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3], stair[2]+stair[3]) # 연속 세 계단 불가.

for j in range(4,n+1):  # 4층 부터 dp 에 저장 시작.
    dp[j] = max(dp[j-3]+stair[j-1]+stair[j], dp[j-2]+stair[j]) # n-1에서 왔을 경우, n-2 에서 왔을 경우 중 max 값 dp[n]에 저장.

print(dp[n])



