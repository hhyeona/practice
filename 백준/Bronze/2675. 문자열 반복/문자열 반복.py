t = int(input())


for _ in range(t):
    s = [list(map(str,input()))]
    N = s[0]

    R = int(N[0])   # 3, 5
    lst = []
    ans = []
    for i in range(2, len(N)):
        st = N[i]
        lst.append(R*st)
    ans = lst
    print(*ans, sep='')