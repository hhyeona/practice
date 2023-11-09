'''
나이순 정렬.
가입한 순서대로 입력.

나이 증가하는 순으로 정렬.
같을 시 가입한 순서대로.

'''
N = int(input())
lst = []
for _ in range(N):
    age, name = map(str,input().split())
    lst.append((int(age), name))

for i in sorted(lst, key=lambda x:x[0]):
    print(*i)