'''
갖고 있는 랜선 수 K,
필요한 랜선 N

1<= k <= 만개.
1 <= n <= 백만개.

항상 k <= n 개 .
랜선 길이 2^31 -1 보다 작거나 같은 자연수.

이분탐색임.

자를 길이 중에 가장 큰 걸 구하는 게 중요.
'''
import sys
input = sys.stdin.readline

def bi(lst,start, end):
    global n
    while start <= end:  #최대값을 구하기 위해서 전체를 돌림.
        mid = (start + end) // 2  # 시작과 끝길이의 중간값을 CM 로 정함.
        cnt = 0
        for i in lst:    # MID 값으로 나눠서 목표 N 만큼 구해지는 지.
            cnt += i // mid

        if cnt >= n:   # 랜선 개수가 같거나 많아지면 CM 를 늘림
            return bi(lst, mid+1, end)
        else:   # 랜선 개수가 목표보다 작으면 CM 를 줄임.
            return bi(lst, start, mid-1)
    return end  # 결국 나오는 end 값이 목표 길이임.


lst = []
k, n = map(int,input().split())
for i in range(k):
    lst.append(int(input().rstrip()))

ans = bi(lst,1, max(lst))
print(ans)



