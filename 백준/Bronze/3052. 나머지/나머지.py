'''
42로 나눔.
'''
lst = []
an = 0
for _ in range(10):
    n = int(input())
    b = n % 42
    lst.append(b)

lst.sort()

ans = 0
for i in range(9):
    if lst[i] != lst[i+1]:
        ans += 1
    an = ans

print(an+1)