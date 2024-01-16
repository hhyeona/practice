'''
나는야 포켓몬 마스터

포켓몬 도감에서
포켓몬의 이름을 보면, 번호를 말하거나 or
번호를 보면, 이름을 말하라.

포켓몬 개수 N, 맞춰야 하는 문제 개수 M 이 주어짐.
1 <= N,M <= 십만

모두 영어. 첫글자 대문자 or 마지막 글자 대문자
2 <= name <= 20

알파벳으로만 들어오면 포켓몬 번호,
포켓몬 번호로만 들어오면 문자 출력.

import sys
input = sys.stdin.readline

word = []
lst = {}
n,m = map(int,input().split())
for i in range(n):
    word.append(str(input().strip()))

for index, w in enumerate(word, start=1):
    lst[w] = index

lst_reverse = dict(map(reversed,lst.items())) # key.value 위치 체인지.

for j in range(m):
    target = input().strip()

    if target.isdigit(): # 여기가 안 먹힘.. 왜 단어인데 여기를 통과하지?
        print(lst.get(target)) # key 값으로 value 출력.

    else:
        print(lst_reverse.get(target))

'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

word_dic = {}
for i in range(1,n+1):
    word = input().strip()
    word_dic[word] = i   # 단어 - 숫자
    word_dic[i] = word   # 숫자 - 단어


for j in range(m):
    target = input().strip()

    if target.isdigit() == True: # isdigit -> O(n)
        print(word_dic[int(target)])

    else:
        print(word_dic[target])
