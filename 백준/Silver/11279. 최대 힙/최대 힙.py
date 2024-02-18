'''
최대 힙.

1. 배열에 자연수 X 넣음.
2. 배열에서 가장 큰 값 추출, 그 값을 배열에서 제거 함.

처음 비어있는 배열에서 시작.

연산 개수 N (십만이하)
x 가 자연수 -> x 값을 넣는 연산.
x 가 0 이면 -> 배열 가장 큰 값 출력 후 제거. (빈 배열일 때는 0 출력)
입력 자연수 2^31보다 작음.

heapq.heappush(heap, item)
heapq.heappop(heap) -  가장 작은 항목 pop, 반환. (기본이 최소 힙임)
 따라서 음수처럼 사용해주면 최대 힙 가능.
'''
import heapq, sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    num = int(input())

    if num != 0:
        # lst.append(num) 대신에
        heapq.heappush(lst, -num) # 원소를 음수로 넣어줘서 최소힙을 최대힙으로 사용.
    else:
        # if len(lst) != 0:
            # mx = max(lst)
            # idx = lst.index(mx)
            # print(lst.pop(idx))  대신에
        if lst:
            print(-heapq.heappop(lst)) # 제일 큰 게 빠지고 프린트 됨.

        else:
            print(0)
