N = int(input())
lst = []

for i in range(1, N+1):  # 약수가 될 수 있는 최솟 값 1부터 자기자신까지 돌려줌. 
    if N % i == 0:       # 약수는 나머지가 0인 것들.
        lst.append(i)    # 하나씩 더해줌. # 자동 정렬됨.


lst_joined = ' '.join(map(str,lst))   #print 함수 위치 주의 
print(lst_joined)