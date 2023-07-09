T = int(input())
N = int(input())
total = 0
ans ='a'
for _ in range(N):
    a, b = map(int,input().split())
    total += a*b

    if total == T:
        ans ='Yes'
    else:
        ans ='No'

print(ans)
