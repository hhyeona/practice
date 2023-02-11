h, m = map(int, input().split())
time = int(input())
v = (m+time)
a = (m+time) // 60
b = (m+time) % 60

if v == 60:
    h = h + 1
    m = v - 60
    if h >= 24:
        h -= 24
elif v < 60:
    h = h
    m = v
else:
    h += a
    m = b
    if h >= 24:
        h -= 24

print(h,m, end =' ')