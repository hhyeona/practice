import sys
input = sys.stdin.readline

i,j = map(int,input().split())
lst = list(map(int,input().split()))
cnt = 0
for k in range(1,j-1):
    left = max(lst[:k])
    right = max(lst[k+1:])
    tm = min(left,right)
    if tm > lst[k]:
        cnt += tm-lst[k]

print(cnt)
