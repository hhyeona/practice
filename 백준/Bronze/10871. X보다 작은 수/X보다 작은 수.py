N, X =map(int,input().split())
arr = list(map(int,input().split()))
lst = []

for i in arr:
    if i < X:
        lst.append(i)

print(*lst)