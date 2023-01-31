chess = [1,1,2,2,2,8] #정상적인 체스 말의 개수.

have = list(map(int,input().split())) # 갖고있는 걸 .split 을 통해 예쁘게 쪼개기
  #리스트로 만들려고(map으로 리스트의 요소를 지정된 함수로 처리하고)(int 정수를 input 받음)

for i in range(6):   # 0~5 까지 (range(n-1) 순서대로 할당해주는 변수 i)
    print(chess[i]-have[i], end=" ") #chess리스트도, have리스트도 각각 range 할 수 있음.
     # end= " "는 print문을 이용해 출력을 완료 한 뒤 내용 수정 가능. 기본 값은 \n 이 들어가 있음.
     # 자매품. sep " " 은 사이에 해당하는 내용 넣을 수 있음. 
    
    # 따라서 , 정답은 숫자들의 띄어쓰기 나열만 나올 것임. 