# 45분 이상이면 -45.
# 44분 이하이면 +15. h는 -1씩
# 0시 44분 이하면, h = 23

H, M = map(int, input().split())

if  M >= 45:
    print(H, M-45)
elif H > 0 and M <= 44:
    print(H-1,M+15)
else:
    print(23, M+15)