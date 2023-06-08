def bubble_sort(N, lst):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
N = int(input())
lst = list(map(int,input().split()))

bubble_sort(N, lst)
print(lst[0]*lst[-1])
