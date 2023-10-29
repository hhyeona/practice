'''
처음 factorial 을 만들어주고,
그 답을 하나씩 리스트에 넣는다.
그 다음 거꾸로 읽으면서 0의 개수를 세고,
0이 아닐 때까지의 개수를 반환함.
'''
# fcatorial 함수
def factorial(number):
    if number == 0 or number == 1:
        return 1

    else:
        return number * factorial(number - 1)

#  입력값 받고 factorial 함수 사용하여 결과 값 구함.
n = int(input())
ans = factorial(n)

# 카운트 하기 위해서 리스트에 넣음.
lst = []
for i in str(ans):
    lst.append(i)

# 리스트 길이 구함.
N = len(lst)

# 마지막 부터 하나씩 불러와서 0인지 비교 하고 cnt 셈
cnt = result = 0
for j in range(N-1, 0, -1):
    if lst[j] == '0':
        cnt += 1
    else:
        break

result = cnt

print(result)