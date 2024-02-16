'''
m미터의 나무를 가져가기 위해
설정할 수 있는 높이의 최댓값.

m 은 20억 이하.

이분탐색.

나무 길이를 이분 탐색으로 찾음.
SUM 을 구하면 됨.
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))

def bi(s,e):
    sum = 0
    mid = (s+e) // 2

    for i in lst: # list에서 하나씩 잘라봄.
        if i > mid:
            sum += (i-mid)

    if sum == m:
        print(mid)
    elif sum > m:
        bi(mid+1, e)
    else:
        bi(s,mid-1)

mx = max(lst)  # 제일 큰 걸 기준으로 함.
bi(0,mx)

위 풀이 시간 초과..
'''
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))

s, e = 1, max(lst)  # 제일 큰 거를 기준으로 시작.

while s <= e:
    sum = 0
    mid = (s+e) // 2

    for i in lst: # list에서 하나씩 잘라봄.
        if i >= mid:
            sum += (i-mid)

    if sum >= m:  # 같아도 최대로 높은 값.
        s = mid + 1
    else:
        e = mid - 1


print(e)  # 결론적으론 S 와 E 가 하나로 귀결됨. # 최댓값이 목표.