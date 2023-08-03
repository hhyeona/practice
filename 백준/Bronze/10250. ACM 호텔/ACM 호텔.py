'''
이걸로 다시 풀어보기..
t = int(input())
ans = 0
num = 0
for _ in range(t):
    h, w, n = map(int,input().split())
    arr = [[0]*(h+1) for _ in range(w+1)]

    for i in range(1,w+1):
        for j in range(1,h+1):
            arr[i][j] += num
            num += 1
            if arr[i][j] == n:
                ans = (i*100)+j
                break


    print(ans)


'''
T = int(input())

for i in range(T):
    h, w, n = map(int, input().split( )) # h=각 호텔의 층 수, w=각 층의 방 수, n=몇 

    floor = n % h 
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    
    print(floor * 100 + room_line)