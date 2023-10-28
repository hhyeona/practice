''''
브루트 포스 : 완전 탐색 알고리즘 종류 중 하나.
brute: 무식한,
force: 힘.
'''
N = int(input())
cnt = 0
result = 666

while True:
    if '666' in str(result):  # string 으로 변환해서 연속된 666이 있는지 확인
        cnt += 1  # 있다면 카운트 늘림.

    if cnt == N: # 카운트가 목표 랑 같다면 종료.
        break

    result += 1  # 원하는 666이 나올 때까지 666에서 +1 씩 함.

print(result)