'''
연원일 순으로 8 자리 날짜가 주어짐.

날짜가 유효하다면 YYYY/MM/DD 형식으로 출력.
유효하지 않다면 -1 출력.
월 : 1~12
일 : 31,28,31,30,31,30,31,31,30,31,30,31

그냥 list 로 안하면 됨.
'''
T = int(input())
for tc in range(1, T+1):
    lst = str(input())  # 아예 문자열 그대로 받음. / list 사용 x
    date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = lst[0:4]    # 슬라이싱함.
    month = lst[4:6]
    day = lst[6:8]
    right = 0  # flag

    if 1 <= int(month) <= 12:  # 월 확인
        for i in range(1,13):  # date 리스트에 맞춰서 index로 달(일) 확인.
            if int(month) == i:  # 1월 ~ 12월달에 속하는 지. 
                if date[i] >= int(day):  
                    right = 1

    if right == 1:
        print(f'#{tc}',year+'/'+month+'/'+day)
    else:
        print(f'#{tc}',-1)


