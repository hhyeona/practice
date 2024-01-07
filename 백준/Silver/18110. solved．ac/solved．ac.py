'''
난이도 정하는 방법

위아래 15퍼 씩 구해서 (반올림)
값들을 빼고 중간에서 평균 값으로 함.
반올림.

import sys
input = sys.stdin.readline

n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

sorted(lst)
discount = round(n*0.15)
del lst[0: discount]
del lst[-1:]

ans = round(sum(lst) / len(lst))
print(ans)

런타임 에러.. 이유가 뭘까?
sort 는 어쩔 수 없어. n 의 갯수 3만개.

## 아직 아무 의견 없는 0 처리도 해줘야 함.
예외 처리를 습관화 하자!

결론 : round 는 사사오입이 아니라 5일 때는 앞자리 숫자 보고 또 달라짐.
그래서 직접 반올림 구현 해야 함.
'''
import sys
input = sys.stdin.readline

# 반올림
def rounded(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)

n = int(input())

if n > 0:  # n 이 0이면 0 처리.
    lst = []
    for i in range(n):
        lst.append(int(input()))

    lst.sort() # 리스트 순서 오름차순 정렬.
    discount = rounded(n*0.15)  # 절삭 값 구함.
    if discount > 0:  # 절삭 값이 0이 아니라면.
        real_lst = lst[discount:-discount]  # 앞 뒤로 제외.
        ans = rounded(sum(real_lst) / len(real_lst))  # 제외한 리스트로 평균 값.
        print(ans)
    else:
        print(rounded(sum(lst)/len(lst)))  # 절삭 값이 0이라면 원래 리스트 평균 값.

else:
    print(0)  # n 이 0이면 의견이 없는거라서 레벨도 0.

