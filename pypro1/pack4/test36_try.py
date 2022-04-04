#에러 발생에 따른 예외 처리
#logic error, exception error : 파일, 네트워크, db, 키보드 등등 예기치 않은 에러에 대처

def divide(a, b):
    return a / b

print("뭔가를 하다가....")
#c = divide(5, 2) #상수가 아니라 입력 값을 받아 동적으로 변하는 입력값이라고 가정하자
#c = divide(5, 0) #ZeroDivisionError: division by zero
#정상 종료를 못 하고 실행을 하다 강제로 종료됨

#작업을 하다가 오류가 발생하면 실행을 가져옴
try:
    c = divide(5, 2)
    #c = divide(5, 0)
    print(c)
    
    aa = [1, 2]
    #print(aa[2])
    print(aa[1])
    
    open("c:/abc.txt")
    
except ZeroDivisionError:
    print("0으로 나눌 수는 없어요")

except IndexError as er: #시스템의 오류 메세지를 전달하고 싶을 때
    print("참조 범위 오류 : ", er)

except Exception as e: #순서 중요 Exception이 있으면 모두 여기서 잡아 먹어서(익셉션 최상위 코드인듯) 위에는 쓰이지 않음
    print("에러 처리 : ", e)

finally: #에러와 상관 없이 무조건 수행되는 문법
    print("에러와 상관 없이 반드시 수행")
    
print("종료")








