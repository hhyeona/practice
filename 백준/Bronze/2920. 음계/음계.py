lst = list(map(int,input().split()))
N = len(lst)
cnt = 0
ans = 'a'
for i in range(N-1):
    if lst[i]+1 == lst[i+1]:
        cnt += 1
        if cnt == N-1:
            ans = 'ascending'

    elif lst[i]-1 == lst[i+1]:
        cnt += 1
        if cnt == N-1:
            ans = 'descending'

    else:
        ans = 'mixed'


print(ans)