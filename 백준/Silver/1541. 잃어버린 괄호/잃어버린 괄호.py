'''
잃어버린 괄호.

양수, +, - 괄호를 가지고 식을 만듦.
괄호를 모두 지움.
다시 괄호를 적절히 쳐서 식의 값을 최소로 만들것임.

0 부터 9, +, - 으로만 이루어짐.
5자리보다 연속 된 숫자는 없음.
0으로 시작 가능.
식의 길이는 50보다 작음.

55-50+40
-35

split 써서 +를 다 더한 후, - 연산 함.
'''
import sys
input = sys.stdin.readline

lst = input().strip().split('-') #['55', '50+40']
target = []

for i in lst:
    sum = 0  # 초기화 중요.
    tm = i.split('+')
    #print(tm) # ['55'] ['50','40']
    for j in tm:
        sum += int(j)
    target.append(sum)

ans = target[0]
for k in range(1,len(target)):
    ans -= target[k]

print(ans)
