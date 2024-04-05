'''
투포인터 : for문 돌면서 또 다른 조건으로 커서가 추가 되는 것.
10개 중에 3개씩 더함. 이런 것

시간 복잡도
for문 : O(N)
각 위치에서 K 개의 값 더함 : O(K)
총 : 0(NK)

10만 x 10 만 >= 2억.

그래서. 처음에 K개의 값을 구함.
For문을 돌면서 다음 인덱스 값 더하고, 앞(이전의)의 값을 뺌.
매 번 최대값을 갱신.
==> for : O(N) * 2
'''
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
lst = list(map(int,input().split()))
ans = 0

# k개 더해주기.
for i in range(k):
    ans += lst[i]

mx = ans

# 다음 인덱스 더해주고, 이전 인덱스 빼주기
for i in range(k,n):
    ans += lst[i]
    ans -= lst[i-k]
    mx = max(mx,ans)

print(mx)