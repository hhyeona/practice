N, K = map(int, input().split())
lst = [i for i in range(1, N + 1)]

ans = []  # 정답 배열
cnt = 0   # 해당(제거) 숫자 index

for _ in range(N): # 숫자 개수만큼 반복하면서 (결국에는 순서만 다를 뿐, 꺼내는 값은 리스트 길이 만큼 임)
    cnt += K - 1 # 0부터 시작하니까 index 를 늘려감.
    if cnt >= len(lst):  # 만약 list 길이를 초과하면
        cnt = cnt % len(lst)  # index 값은 기존 더해서 초과한 index 값을 실시간으로 pop 된 리스트 길이로 나누면 다시 한바퀴 돈 리스트 값이 됨.

    ans.append(str(lst.pop(cnt))) # 정답 배열에 pop으로 해당 번호 제거한 걸 넣음.
print("<", ", ".join(ans)[:], ">", sep='')