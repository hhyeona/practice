'''
find()
- 찾을 문자, 시작, 끝 3개 파라미터 가능.
S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')
    
index()
- list 의 index 숫자 반환.
'''
s = list(input())
al = 'abcdefghijklmnopqrstuvwxyz'

for i in al:
    if i in s:
        print(s.index(i), end=" ")

    else:
        print(-1,  end=" ")

