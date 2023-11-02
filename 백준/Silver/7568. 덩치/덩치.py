'''
덩치.

유레카 - 문제 설명에 답이 있다.

N 명의 집단에서 각 사람의 덩치 등수는
자 . 신 . 보 . 다 . 더 . 큰 . 덩치의 사. 람 . 의 . "수" 로 정해진다.
즉, cm / kg 모두 큰 사람의 수를 구해서 +1 한게 나의 등수인 셈!!!

막 계산할라 그랬어. ㅠㅠ 그러지 말고 문제에 답이 있다!!
'''
N = int(input())
kgcm = []
ans = []
for _ in range(N):
    k, c = map(int,input().split())
    kgcm.append((k,c))



for i in range(N):
    cnt = 0
    for j in range(N):
        if kgcm[i][0] < kgcm[j][0] and kgcm[i][1] < kgcm[j][1]:
            cnt += 1

    ans.append(cnt+1)

print(*ans)