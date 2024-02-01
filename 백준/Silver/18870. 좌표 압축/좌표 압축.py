'''
문제 뜻을 잘 모르겠음.

결론은 작은 순서대로 순위를 index에 맞춰서 출력하라.
set 써서 중복 제거해야함.
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
alst = sorted(set(lst))
dic = {}
for i in range(len(alst)):
    dic[alst[i]] = i

for j in lst:
    print(dic[j],end=" ")
