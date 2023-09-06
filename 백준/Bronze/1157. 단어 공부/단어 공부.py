'''
단어 공부 
대문자로 uppper()
대문자 맞는지 isupper()
소문자로 lower()
소문자 맞는지 islower()
set() 중복 허용하지 않음. 순서가 없음. 
인덱싱으로 접근하려면 리스트 or 튜플로 변환 후 사용.
s1 = set([1,2,3])
l1 = list(s1)
print(l1)		# result : [1,2,3]
print(l1[0])		# result : 1
'''
st = input()   #Mississipi
ST = st.upper()  
# input().upper() 로 바로 해도 됨.
stlst = list(set(ST))  #['M', 'P', 'S', 'I']

cnt= []
for i in stlst:
    cnt.append(ST.count(i))  #[4, 4, 1, 1]

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(stlst[(cnt.index(max(cnt)))]) 


