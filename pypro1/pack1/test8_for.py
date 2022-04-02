#반복문 for : for문의 형식 for target in 묶음형object:(묶음형 객체) .......

#list
for i in [1, 2, 3, 4, 5]:
    print(i, end = " ") #i는 차례대로 1~5까지의 수를 가짐 묶음형 요소의 갯수만큼 값을 i는 받을 수가 있음

print()

for _ in [1, 2, 3, 4, 5]: #값을 받지 않으려면 '_'를 사용
    print("반복") #변수명을 '_'를 사용하면 값을 받는 것이 아니고 요소의 갯수 만큼 실행

print()
#tuple
for i in(1, 2, 3, 4, 5):
    print(i, end = " ")

print()
#set
for i in{1, 2, 3, 4, 5}: #set은 순서가 없어서 순서대로 나오지 않을 가능성이 높다
    print(i, end = " ")

print()
#dict
soft = {"java":"웹용", "python":"만능", "oracle":"데이터베이스"}
for i in soft.items(): #dict는 key와 value로 묶여 있고 그것을 가져오려면 items를 사용해야 함
    print(i, end = " ") #tuple 타입으로 값을 리턴한다
    print(i[0], i[1]) #인덱스 0번이 "java" 1번이 "웹용" -> 이런식으로 해석도 가능함

print("--------")
for i in soft.keys(): #변수 soft의 key 값을 얻어올 수가 있다
    print(i, end = " ")

print("--------")
for i in soft.values(): #변수 soft의 value 값을 얻을 수가 있다
    print(i, end = " ")

print("--------")
for k, v in soft.items(): #인덱스를 이렇게 활용하면 key와 value 값을 나눌 수가 있다
    print(k) #soft.items를 사용하면 key값과 value 값을 사용할 수가 있는데 key:value 형식이라 key의 인덱스
    print(v) #value의 인덱스

print()
li = ["a", "b", "c"] #list형식
for idx, data in enumerate(li): #enumerate은 내장형 obj 이렇게 하면 인덱스까지 얻을 수가 있다
    print(idx, ")", data)

print()
#구구단 2단과 3단만 찍어보기
for n in [2,3]:
    print("--{}단--".format(n)) #맷팅 시 .fotmat의 중괄호를 사용하면 1개만 사용될 땐 알아서 맵핑됨
    for i in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(n, i, i*n)) #{0} 은 인덱스 0번째, format(n, i, i*n) 에서 n을 맵핑함

print()
datas = [1, 2, 3, 4, 5]
for i in datas:
    print(i, end = " ")
else: #자주 사용되지는 않지만 for문에 else도 사용됨
    print("정상 종료일 때 수행") #for문이 정상적으로 종료가 돼서 else까지 넘어와 수행이 되는 것

print()
datas = [1, 2, 3, 4, 5]
for i in datas:
    if i == 2:    continue #i가 2가 될 때 하단의 문단을 수행하지 않고 자신이 속해있는 맨 최상단으로 이동함
    #if i == 4:break #i가 4가 될 때 반복문을 강제로 빠져나감 
    print(i, end = " ")
else: #자주 사용되지는 않지만 for문에 else도 사용됨
    print("정상 종료일 때 수행") #브레이크만 안 나오면 나옴

print()
jumsu = [95, 70, 60, 50, 100]
number = 0

for jum in jumsu:
    number +=1
    if jum < 70: continue
    print("%d번은 합격" %number)

print()
li1 = [3, 4, 5]
li2 = [0.5, 1, 2]
result = []
for a in li1:
    for b in li2:
        print(a + b, end = " ") #이 수를 다른 변수에 담고 싶으면
        result.append(a + b) #묶음형 변수 list인 result에 맨 끝에서부터 하나씩 넣음

print(result)

#위에와 같은 값을 출력하는 문장
print()
datas = [a + b for a in li1 for b in li2] #리스트내포
print(datas)










