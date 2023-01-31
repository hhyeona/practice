# 주어진 숫자 부터 거꾸로 출력하기. 목표.

# 숫자 int 받아야지. input 을 int 형으로 입력 받아. 
# 빈 리스트에 만들어준다. 
# 0~n 까지 반복문을 list에 append로 더해준다.
# 만들어진, 리스트를 역순으로 바꾸기 위해, 바꾸는 리스트의 함수를 쓴다. (검색해봐^^)
# 리스트 프린트. 

# range로 하면 0부터 시작인데, n+1 까지 해줘야 함..?
# sorted 하면 오름차순, reverse 하면 내림차순으로 바뀜.


num = int(input())      #정수 입력 받기.

lst = []    #빈 리스트 만들기. 리스트형이라 메서드 쓸 수 있음(append) 


for i in range(0, num+1):  # 0~num 까지 순서대로 i 에 넣고
    lst.append(i)         # 빈 리스트에 append 로 하나씩 더해줌.

lst.sort(reverse=True)  # 완성된 리스트를 기본 값인 오름차순인 sort에 reverse 를 True로 하면 역순이 됨. 


print(*lst)



    #print(sorted((i), reverse=True))


