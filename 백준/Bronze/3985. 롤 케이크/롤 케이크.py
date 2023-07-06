L = int(input()) # 롤케이크 길이
N = int(input()) # 인원 수 
lst = [1] * (L+1)  # 롤케이크 한 조각씩
mx1 = mx1_i = mx2 = mx2_i = 0
for i in range(1, N+1):  # 인원 수 만큼 인풋값
    s, e = map(int,input().split()) # 처음과 끝 번호
    if mx1 < (e-s+1):   # 제일 많은 양 갱신 (번호-번호+1  해줘야 진짜 조각 수 나옴.)
        mx1, mx1_i = (e-s+1), i
        
    cnt = sum(lst[s:e+1])  # 실제로 받은 케이스 수의 합 [리스트 길이 세기]
    if mx2 < cnt:
        mx2, mx2_i = cnt, i
    lst[s:e+1] = [0]*(e-s+1)  # 실제로 받은 구간은 0으로 갱신
    
    
print(mx1_i)
print(mx2_i)