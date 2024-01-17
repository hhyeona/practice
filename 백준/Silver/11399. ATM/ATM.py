'''
ATM

N 명. 돈 일출 Pi 분.
각 사람이 돈을 인출하는 데 필요한 시간의 합의 최솟값.

빨리 끝나는 사람부터 하면 됨.

import sys
input = sys.stdin.readline

person = {}
n = int(input())
lst = [0]+list(map(int,input().split()))

for i in range(1, n+1):
    person[i] = lst[i]

ans = sorted(person.items())
print(ans)

index,time 딕셔너리.
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

lst.sort()
ans = 0
for i in range(1,n+1):
    ans += sum(lst[0:i])  #0번부터, i 번씩 늘려서 더했을 뿐.

print(ans)
