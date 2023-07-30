N = int(input())
target = []   # 우선, 오름차순으로 1~N 만큼 넣을 스택.
ans = []   # "+" or "-" 값을 넣을 스택.
flag = 0
t = 1  # 1부터 오름차순으로 넣으니까.
for _ in range(N):
    n = int(input())
    while t <= n :  # 오름차순 push 니까 1부터 push, 이 때 입력한 수 만날 때 까지만 push.
        target.append(t)     #
        ans.append("+")
        t += 1

    if target[-1] == n:  # 원하던 숫자 pop
        target.pop()
        ans.append("-")

    else:
        print("NO")    # 마지막이 원하던 숫자보다 크다면 원하던 건 그 밑에 있어서 완성될 수 없다.
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i)