'''
위상정렬? 삽입정렬!
lst.remove(lst[i])
lst.insert(1,lst[i])
-> 실제로 정렬 안해도 됨.
cnt만 해주면 끝.
'''
import sys
input = sys.stdin.readline

n = int(input())
for tc in range(1,n+1):
    lst = list(map(int,input().split()))[1:]
    cnt = 0
    for i in range(1,20):
        for j in range(i):
            if lst[j] > lst[i]:
                cnt +=1

    print(tc,cnt)


