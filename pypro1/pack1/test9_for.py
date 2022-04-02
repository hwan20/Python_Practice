#반복문 for : for문의 형식 for target in 묶음형object:(묶음형 객체) .......

#웹에서 읽은 자료라고 가정 한다
#공백으로 단어 분리
#여러 줄을 입력하려면 """ """ 로

ss = """내연기관을 고집하던 마세라티가 고고함을 내려놓고 전동화를 마음먹었다는 것 자체가 큰 변화다.
 마세라티는 최근 2030년까지 내연기관차 생산을 중단하고 모든 차량을 전기화한다고 발표했다.
 전동화 첫 단계로 마세라티가 내놓은 브랜드 최초의 전동화 모델 기블리 하이브리드와 서울 한남동에서 안동 군자마을까지
 마세라티는 최근 2030년까지 내연기관차 생산을 중단하고 모든 차량을 전기화한다고 발표했다.
 전동화 첫 단계로 마세라티가 내놓은 브랜드 최초의 전동화 모델 기블리 하이브리드와 서울 한남동에서 안동 군자마을까지
 약 260km를 동행하기 위한 시동을 걸었다."""

import re #정규표현식을 사용하기 위해서 re를 사용
#\s는 공백이나 탭
ss2 = re.sub(r"[^가-힣\s]", '', ss) #한글과 공백을 제외한 나머지를 없앰
print(ss2)

print()
ss3 = ss2.split(sep=" ")
print(ss3) # ss2의 문자열을 공백이 있을 때마다 list형식으로 나눔

print()
print(len(ss3)) #묶음 문자열의 길이
print(len(set(ss3))) #중복된 단어를 제거한 문자열의 길이

cou = {} #단어의 발생 횟수를 dict로 저장
for i in ss3: #i에 ss3값이 하나씩 들어오고
    if i in cou: #들어온 ss3 값을 dict 타입인 key : value 형식으로 저장하고 비교함
        cou[i] += 1
    else:
        cou[i] = 1 # {"키" : i} 최초로 나온 값이면 value를 누적 아니면 key를 누적
print(cou)

#공백으로 나눈 문자열이 cou에 없으면 (else이면) key 값에 1을 출력 있으면 value에 1을 누적


print()
for test in ["111-1234-0000", "일이삼-사오육칠-팔구십영", "2222-3333"]:
    if re.match(r"^\d{3}-\d{4}-\d{4}$", test):
        print(test)
    elif re.match(r"^[가-힣]{3}-[가-힣]{3,4}-[가-힣]{4}$", test):
        print(test)
    else:
        print("전화 번호 형식으로 입력하세요")

print()
a = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)
#위와 같음
print(list(i for i in a if i %2 == 0))

print()
datas = [1, 2, "a", True, 3.4]
li = [i for i in datas if type(i) == int]
print(li)

print()
datas = {1, 1, 2, 2, 3} #set은 중복 허용을 하지 않아 1, 2, 3으로 나옴
se = {i * i for i in datas} #i에서 1이 나올 때 1*1이 됨 3이 나왔으면 3*3
print(se)

print()
id_name = {1:"tom", 2:"james"}
name_id = {value:key for key, value in id_name.items()} # dict의 데이터를 key 1 : value "tom" 으로 담고 value:key 로 저장을 했으니 위치가 바뀜 
print(name_id)

print()
temp = [1, 2, 3, 3]
for i in temp:
    print(i, end = " ")
print()
print([i for i in temp]) #list로 출력 가능
print({i for i in temp}) #set으로 출력 가능

print()
#과일 값 계산
price = {"사과" : 2000, "오렌지" : 1000, "배" : 3000}
guest = {"사과" : 2, "배" : 1, "오렌지" : 1} #두 dict들을 맷팅하여 사용하기 때문에 key 값은 서로 같아야 된다 key 값에 따라 맷팅되기 때문에 순서 상관 X
bill = sum(price[f] * guest[f] for f in guest) #sum은 내장 함수로 요소들의 합을 구함
#제너레이트 객체가 생성됨 사과부터 배까지 순서대로 값을 입력하고 key값에 맞게 맷팅이 되어 값을 구할 수가 있다
print(bill)




