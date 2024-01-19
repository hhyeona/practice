'''

피보나치 중
0 1 출력되는 횟수 공백으로 구분해서 출력.

n <= 40.

재귀함수 계속 돌리는 것보다 DB로 넣어두는 게 낫나? => 다이나믹 프로그래밍
재귀로만 하면 시간 제한 될 것 같음.

DP(한번 구한 결과 값 저장해두고 재사용) O(N*2) -> O(f(n))
조건.
1. 겹치는 부분문제 Overlapping subproblems 
  : 동일한 작은 문제들이 반복하여 나타나는 경우.
2. 최적 부분 구조 Optimal substructure
  : 부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있는 경우.

이 문제에서는 피보나치가 아니라 0과 1을 구해야 함.
fibonacci(n) = fibonacci(n-1)+fibonacci(n-2) 개념.
0,1 의 호출 횟수 => (피보나치 n-1 에서 0,1 의 호출횟수) + (피보나치 n-2 에서 0,1 호출 횟수) 를 배열에 추가.
'''
import sys
input = sys.stdin.readline


zero = [1,0,1] # index is f(index).
one = [0,1,1]   # index 마다 앞에 두 index를 더한 값이 됨.

def fibo(number):
    length = len(zero)  # 들어온 target 넘버가 index 보다 높으면 새로 구해야 함.
    if number >= length :
        for i in range(length, number+1):  # zero,one 에 없는 정보 더해주기
            zero.append(zero[i-1]+zero[i-2])  #그 전의 정보들로 새로운 0 과 1 더해감.
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[number], one[number]))  # target에 해당하는 index를 출력.


T = int(input())
for _ in range(T):
    target = int(input().strip())

    fibo(target)
