'''
N 개의 숫자 공백 없음. 모두 합한 값 출력.
'''
N = int(input())
ans = 0

llst = [list(map(int,input()))]
lst = llst[0]

for i in lst:
    ans += i

print(ans)