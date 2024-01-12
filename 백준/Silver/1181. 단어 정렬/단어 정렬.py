'''
단어 정렬

길이 짧은 것 부터.
같으면 사전 순으로 (SORT 가 해줌)
단, 중복 제거 (SET)
'''
import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(str(input().rstrip()))  # 끝 개행 삭제

ans = set(lst)  # 중복 제거 {}
lst=list(ans) # 다시 리스트 변환
lst.sort()    # 알파벳 순서대로 sort
lst.sort(key=len)  # 길이로 다시 sort

for i in lst:
    print(i)