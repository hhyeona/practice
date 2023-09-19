'''
달팽이는 올라가고 싶다.
나무 막대 : V  미터

낮에 +A 미터
밤에 -B 미터 
시간초과 -> 

도달 하는 날 x 일 ; 총 올라가는 횟수는 x 번, 내려오는 횟수는(x-1)번.

Ax - B(x-1) = V 가 됨. 
x = (V-B)/(A-B)  가 됨.
즉, x 가 7.0이면 7일만임. 
그런데 7.8 이러면 8일 만이겠지. 
'''
a, b, v = map(int,input().split())

x = (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x)+1)

