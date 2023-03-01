N, M = map(int,input().split())
lst = list(map(int,input().split()))
rlt = 0
mx = 0

for i in range(0,N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            # print(i,j,k)
            sm = lst[i] + lst[j] + lst[k]
            # print(sm)
            if sm <= M:
                rlt = max(rlt,sm)
               
print(rlt)
