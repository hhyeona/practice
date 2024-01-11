'''
1<=M<=N<= 1백만.

n,m 사이 소수 세로로 하나씩 출력.  ( n 까지 할 필요 없고 제곱근 까지 하면 됨!)
def prime_number(n):
    for i in range(2,n):
        if n % i == 0:
            return False

    return True  # False 가 되지 않고 for문을 빠져나왔다면 소수임.


n, m = map(int,input().split())

ans = []
for j in range(n, m+1):
    if prime_number(j) == True:
        print(j)

시간초과 남... 짝수와 같은 약수 있는 Number 를 제거해야함.
'''
def prime_num(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):  # 번호 당 끝까지 나눠보는 게 아니라, 제곱근까지만 구하면 약수 절반으로 알 수 있음.
        if n % i == 0:
            return False

    return True

n, m = map(int,input().split())

for j in range(n, m+1):
    if prime_num(j):
        print(j)

