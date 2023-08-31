'''
각 자리 제곱 수 더한 합에서 10으로 나눈 나머지.
'''
lst = list(map(int,input().split()))
total = 0

for i in range(5):
    num = lst[i]
    total += (num*num)

ans = total % 10

print(ans)