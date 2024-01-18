'''
비밀번호 찾기

저장된 사이트 주소 수 1 <= n <= 십만.
비밀번호 찾으려는 사이트 주소 수 1 <= m <= 십만.

n 줄에 걸쳐.
사이트 주소 비밀번호   공백으로 구분. (사이트 주소 중복 x), 비번 (최대 20자)

딕셔너리
'''
import sys
input = sys.stdin.readline

arr = {}
n,m = map(int,input().split())

lst = []
for _ in range(n):
    lst.append(input().split())

for site, bi in lst:  # 리스트에서 사이트 주소와 비번을 딕셔너리 형태로 저장.
    arr[site] = bi

ans = []
for i in range(m):
    target = input().strip()

    if target in arr:    # 딕셔너리에서 해당 키로 비번 저장.
        ans.append(arr[target])

for i in ans:
    print(i)