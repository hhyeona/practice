def solution(price, money, count):
    answer = -1
    tm = 0
    for i in range(1,count+1):
        tm += price * i
        if money > tm:
            answer = 0
        else:
            answer = tm - money
    return answer