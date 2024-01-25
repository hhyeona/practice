'''
알파벳을 숫자로 변환.

알파벳으로 이루어진 문자열을 입력 받아
각 알파벳을 1 부터 26까지 숫자로 변환하여 출력.

문자열 최대 길이 200.

# 아스키코드 065 ~ 090 A~Z
# 097~122 a ~ z
'''
al = input()
# alpha = []
# for i in range(65,91):  # 알파벳 리스트 만들기.
#     alpha.append(chr(i))

alpha = [chr(i) for i in range(65,91)]
ans = []
for i in al:
    for j in range(26):
        if i == alpha[j]:
            ans.append(j+1)

print(*ans)