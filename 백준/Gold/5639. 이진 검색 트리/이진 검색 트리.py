import sys
sys.setrecursionlimit(10**5)
def post(s, e):           # 파라미터로 시작점과 끝점 index. 변수 명 설정. (구간 의미!!!// 노드 말고)
    if s > e:        # 범위를 벗어나면 안되니까. (ex)98 이후로 오른쪽 자식 노드들이 없을 경우 )
        return

    root = lst[s]          # 일반화 (루트는 계속 시작점으로 갱신되어야 함)
    # print(root)
    num = 0
    flag = 0               # 오른쪽 자식들이 없을 경우 확인해주려고 
    for idx in range(s,e+1):
        if lst[idx] > lst[s]:
            num = idx
            flag = 1
            break

    if flag == 0:         # 오른쪽 자식이 없다면, 
        num = e+1

    post(s+1,num-1)          #왼쪽 자식들 호출
    post(num,e)              #오른쪽 자식들 호출
    print(root)



lst = []       #입력값 리스트로 만들기.
while True:                         # 입력 길이가 정해져 있지 않으므로 예외처리로 입력받음.
    try:
        node = int(input())         # = lst.append(int(input())) 해도 됨.
        lst.append(node)            # 하나씩 입력받은 걸 리스트에 더해줌.

    except:
        break
N = len(lst)
post(0,N-1)
