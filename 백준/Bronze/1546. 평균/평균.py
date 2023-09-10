'''
평균
'''
n = int(input())
lst = list(map(int,input().split()))

m_score = max(lst)
new_list = []
for i in range(n):
    if lst[i] <= m_score:
        new = (lst[i]/m_score*100)
        new_list.append(new)

ans = 0
for j in range(n):
    ans = sum(new_list)

print(ans/n)
