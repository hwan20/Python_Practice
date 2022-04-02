#python의 if


var = 5
if var >= 3: #조건 다음에는 :이 있다 
    print("크구나") #여기까지가 if문 블럭. var = 2일 때 if문이 실행하지 않음
    
print("참일 때 수행")

print("end1")

print()    

var = 5
if var >= 3:
    #print("크구나2")
    pass #조건이 참일때 아무것도 수행하지 않고 싶지 않으면 pass를 사용
else: #python에서 else문
    print("작구나2")
    print("작구나2")
print("참일 때 수행")

print("end2")

print()

money = 499
age = 23
#if문 안에 if문이 들어가 있는 다중 if문
if money >= 500:
    item = "apple"
    if age <= 30:
        msg = "young"
    else:
        msg = "old"
else:
    item = "orange"
    if age > 20:
        msg = "man"
    else:
        msg = "child"

print(item, msg)

print()

jum = 70
#jum = int(input("점수 입력 : ")) #input으로 점수를 입력받을 수도 있다 입력 받은 점수는 str이라서 int로 바꿔준다
#print(jum, type(jum))
res = "" #res에 공백을 넣어 데이터를 입력 받는다

if jum >= 90:
    res = "a"
elif jum >= 70:
    res = "b"
else:
    res = "c"
print("res : " + res)

#위와 아래는 같음

if 90 <= jum <= 100:
    res = "a"
elif 70 <= jum < 90:
    res = "b"
else:
    res = "c"
print("res : ", res)

print()
names = ["정화", "재이", "일환"]
print(names[0])
if "재이" in names: # 이름과 in 앞에 not을 붙이면 부정문이다
    print("{} 친구야~" .format(names[0])) #names에 '재이' 가 있으면 '친구야~'를 리턴한다
else:
    print("누구?")

print()

a = "kbs"
b = 9 if a == "kbs" else 11 #b는 if의 값에 따라 9와 11 둘 중에 하나를 치환받는다 참이면 앞에 거짓이면 뒤에
print(b)

a = 11
b = "mbc" if a == 9 else "kbs" #a는 0보다 크니 false가 되어 kbs가 출력
print(b)

print()

a = 3
if a < 5:
    print(0)
elif a < 10:
    print(1)
else:
    print(2)

#위와 아래는 같다
print(0 if a < 5 else 1 if a< 10 else 2 ) #이렇게 길어지면 잘 사용은 안 함

print()
res = a * 2 if a > 5 else a + 2
print(res)

print((a + 2, a * 2)[a > 5]) #거짓이면 [0], 참이면 [1] 








