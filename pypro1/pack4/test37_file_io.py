#파일 단위로 읽고 저장
import os #시스템이 가지고 있는 정보를 가지고 올때 쓰임
from _ast import Try

print(os.getcwd()) #현재 파일의 경로를 알려줌

#mode 'r'은 읽기 'w'는 저장 

try:
    print("파일 읽기") 
    #f1객체가 open 명령어를 따라 객체를 생성함        mode는 = 'r', 'w', 'a', 'b'(는 +'b'로 사용됨) 등이 있다
    #f1 = open(r"C:\work\repo\pypro1\pack4\abc.txt", mode="r", encoding="utf-8")
    #f1 = open(os.getcwd() + r'\abc.txt', mode="r", encoding="utf-8")
    f1 = open('abc.txt', mode="r", encoding="utf-8") #경로가 같으면 앞에 생략 가능하다
    print(f1)
    print(f1.read()) #파일을 읽기
    f1.close() #파일을 닫지 않아도 되지만 효율성이 떨어지니 닫기
    
    print("파일 저장")
    f2 = open('abc2.txt', mode="w", encoding="utf-8")
    f2.write("my friend\n")
    f2.write("tom, 한국인")
    f2.close()
    print("저장 성공")
    #계속 실행하면 덮어쓰기 함
    
    print("파일 추가") #파일에 내용 추가 append와 같이 뒤에서부터 넣음
    f3 = open('abc2.txt', mode="a", encoding="utf-8")
    f3.write("\n오공")
    f3.write("\n팔계")
    f3.write("\n삼장")
    f3.close()
    print("추가 성공")
    
    print("파일 읽기")
    f4 = open('abc2.txt', mode="r", encoding="utf-8")
    print(f4.readline()) #한 줄씩 읽기
    print(f4.read()) #몽땅 읽기
    f4.close()
    
except Exception as e:
    print("에러 : ", e)

#파일에서 with문 사용하면 close안 해도 된다 알아서 닫아줌.
print("파일 처리 계속 ------- with문 사용") #with 블럭을 사용 파일에서만 사용하는 것은 아님
try:
    with open("abc3.txt", mode="w", encoding="utf-8") as ff1:
        ff1.write("파이썬으로 문서 저장\n")
        ff1.write("with문을 사용하면\n")
        ff1.write("명시적으로 close()할 필요가 없다\n")
    print("저장 완료")
    
    with open("abc3.txt", mode="r", encoding="utf-8") as ff2: #binary형식으로 저장하려면 mode="rb" 이렇게 저장한다
        print(ff2.read())

except Exception as e2:
    print("에러 : " + str(e2))

print("파일 처리 계속 ------- pickle (모듈 사용)문 사용 : 객체를 파일로 저장") #데이터 분석이나 DB에서 사용 
import pickle

try:
    #이러한 파일을 저장하고 싶다
    dictData = {"tom" : "1234-5678", "james" : "1111-2222"} 
    listData = ["채원", "해승"]
    tupleData = (dictData, listData)
    
                        #파일 확장자명 아무렇게나? write를 binary 형태로 하니 
    with open(file="hello.dat", mode="wb") as ff3: #binary mode doesn't take an encoding argument
        pickle.dump(tupleData, ff3) #저장할 때 쓰는 것 dump
        pickle.dump(listData, ff3)
    
    print("개체를 파일로 저장")
    
    with open(file = "hello.dat", mode = "rb") as ff4:
        a, b = pickle.load(ff4)
        print(a) #11시 40분
        print(b)
        c = pickle.load(ff4)
        print(c)
    
except Exception as e3:
    print("에러3 : " + str(e3))






