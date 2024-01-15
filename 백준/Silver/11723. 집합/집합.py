'''
집합.
{}
비어있는 공집합 S 주어짐.
add x : S 에  x 추가.
remove x : S에 x 제거.
check x : S에 x 있으면 1, 없으면 0 출력.
toggle x : S에 x 가 있으면 x를 제거, 없으면 x 를 추가한다.
all : S를 {1,2,3,..,20} 으로 바꿈.
empty: S 를 공집합으로 바꿈.

연산의 수 M <= 3백만.

check 연산이 주어질 때마다, 결과 출력 함.

add() : 특정 값 추가.
update() : 여러 개 값을 추가 함. 리스트로 넣어야 함.
remove() : 특정 값 삭제함 (집합 안에 해당 원소가 없을 시 오류)
discard() : 특정 값 삭제함 (집합 안에 값이 없어도 정상작동 됨)
'''
import sys
input = sys.stdin.readline

lst = set()
N = int(input())
for _ in range(N):
    tm = input().strip().split()
    if len(tm) == 1:
        if tm[0] == 'all':
            lst = set([i for i in range(1, 21)])
        if tm[0] == 'empty':
            lst = set()

    else:
        w, x = tm[0], tm[1]
        x = int(x)

        if w == 'add':
            lst.add(x)
        if w == 'remove':
            lst.discard(x)
        if w == 'check':
            if x in lst:
                print(1)
            else:
                print(0)
        if w == 'toggle':
            if x in lst:
                lst.discard(x)
            else:
                lst.add(x)