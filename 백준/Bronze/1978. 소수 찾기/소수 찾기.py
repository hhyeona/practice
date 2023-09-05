'''
소수 찾기
소수 특징.
1. 1보다 큼
2. 약수가 1과 자기 자신임. ( 약수의 대칭성이 없으면 됨)
소수 판별법 (시간복잡도: O(n−−√))
def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0 :
            return  #false
        i += 1
    return # true
'''
def primality(n):
    i = 2
    global ans
    while i * i <= n:
        if n % i == 0:
            return #false
        i += 1
    ans += 1
    return ans  #true

n = int(input())
lst = list(map(int,input().split()))
ans = 0
for j in lst:
    if j != 1:
        primality(j)

print(ans)