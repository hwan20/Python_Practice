#Thread
#process는 실행 가능한 파일을 말한다. 프로세스는 현재 실행 중인 프로그램을 의미하며 task라고도 부른다.
#process는 작은 실행단위를 thread라고 한다. thread기법을 이용하면 여러 개의 thread를 통해 여러 작업을 할 수 있다
#multi thread에 의한 multi tasking이 가능함

#multi process는 한 번에 여러 파일을 돌리는 것이 아닌 파일을 돌리다 남는 순간 순간 다른 파일을 돌리는 것을 뜻한다
#하지만 속도가 너무 빨라 우리 눈에는 한 번에 동시에 실행하는 것처럼 보일 뿐이다

import threading, time

def run(id):
    for i in range(1, 11):
        print("id : {}-->{}".format(id,i))
        time.sleep(0.5) #0.5초 마다 진행됨 자바에서는 thread로 시간줌

#1) thread를 사용하지 않은 경우
#순차적으로 진행해서 "일" 이 먼저 끝나야 "이"가 진행됨
#run("일") # 순차적
#run("이")

#2) thread를 사용하는 경우
th1 = threading.Thread(target = run, args = ("일",)) #Thread 클래스를 생성자로 해서 객체를 생성함
th2 = threading.Thread(target = run, args = ("이",)) #run 함수의 아규먼트 즉 인자에 "이" 를 넣음
#thread는 start를 해야 시작
th1.start()
th2.start()

#join을 사용하면 메인 thread가 실행되지 않고 기다림
th1.join()
th2.join()

#첫 번째 thread가 실행되고 넘어갈 때 두 번째 thread를 실행함
#동시 실행이 아니고 현재 실행하는 것이 없을 때 다음 것을 실행하는 것
#thread는 랜덤적으로 실행됨

#끝나고 프로그램이 종료되는 것이 아님 메인도 thread로 관리돼서 같이 동작됨
print("프로그램 종료") 




