N = int(input())
lst = list(map(int, input().split()))
tar = int(input())
a = len(lst)
cnt = 0

for i in range(a):
    if lst[i] == tar:
        cnt += 1

    
print(cnt)