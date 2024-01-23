'''
조합론

중복되지 않는 선에서 조합문제.

Tc = 최대 100
가진 의상 수 0 <= n <= 30
모든 문자열 20이하의 소문자. 같은 이름은 없음.

종류별로 개수 + 1(안입는경우)
즉, (2종류 + 1) * (1종류 + 1)
에서 마지막으로 다 안입는 경우를 제외해야 함. -1
(하나라도 입고 있어야 하는 조건)
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    clothes = {}
    for i in range(N):
        type = list(input().split())  #{'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}
        if type[1] in clothes:   # type 이미 존재한다면, 그 딕셔너리에 추가
            clothes[type[1]].append(type[0])
        else:               # type 이 존재하지 않다면, 추가.
            clothes[type[1]] = [type[0]]

    # for i in range(N):
    #     a , type = input().split()  # {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}
    #     if type in clothes.keys():
    #         clothes[type].append(a)
    #     else:
    #         clothes[type] = [a]

    cnt = 1
    for j in clothes:  # j is keys.
        cnt *= (len(clothes[j])+1)
    print(cnt-1)