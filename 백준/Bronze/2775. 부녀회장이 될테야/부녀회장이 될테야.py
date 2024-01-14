'''
부녀회장이 될테야

1 <= k,n <= 14

'''
tc = int(input())

for _ in range(tc):
    k = int(input())
    n = int(input())
    f0 = [i for i in range(1,n+1)]  #0층 리스트 만들어 놓고

    for j in range(k): # 층 만큼 반복
        for k in range(1,n): # 1호 ~ n 호까지. (인덱스로 사용해서 n 까지임)
            f0[k] += f0[k-1]
    print(f0[-1])