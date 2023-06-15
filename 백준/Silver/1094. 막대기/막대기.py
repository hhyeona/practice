'''
64 32 16 8 4 2 1 중에 몇 개가 해당되는지 라서 
이진법으로 접근하면 됨. 1의 개수 구하는 것. 
'''
a = int(input())
cnt = 0
while a != 0:
    if a % 2 == 1:
        cnt += 1
    a = a // 2
print(cnt)
