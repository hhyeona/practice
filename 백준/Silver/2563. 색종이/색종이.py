N = int(input())
arr = [[0]*100 for _ in range(100)]
cnt = 0

for _ in range(1, N+1):
    r1,c1 = map(int,input().split())

    for _ in range(1,N+1):
        for i in range(r1,r1+10):
            for j in range(c1,c1+10):
                arr[i][j] += 1

for i in range(100):
    for j in range(100):
        if arr[i][j] != 0:
            cnt += 1

print(cnt)
