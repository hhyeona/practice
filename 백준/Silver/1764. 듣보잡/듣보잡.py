'''
듣보잡

듣도 못한, 보도 못한 명단.
듣도, 보도 못한 명단 구하기.

듣도 못한 N, 보도 못한 M
N 개 줄
N+2 줄부터 주어짐.
이름 <= 20
n,m <= 50만.
중복은 없음.

명단을 사전순으로 출력.

그냥 하면 시간초과 남.
집합 자료형 set 을 사용해서 교집합을 꺼내야 함.
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

hear = set()
see = set()

for _ in range(n):
    hear.add(input().strip())

for _ in range(m):
    see.add(input().strip())

ans = sorted(list(hear & see))

print(len(ans))
for i in ans:
    print(i)