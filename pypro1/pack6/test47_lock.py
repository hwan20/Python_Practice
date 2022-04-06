import threading, time
from threading import Thread, Condition


g_count = 0 #전역 변수는 자동으로 스레드의 공유자원이 된다
            #2개 이상의 스레드가 이 변수를 사용한다
lock = Condition() #스레드 공유 자원 접근에 제한을 강제하기 위한 잠극 객체이다

#잠금객체 사용하기 전
def threadCount(id,count):
    global g_count #변수 앞에 global 명령어가 있으면 함수 내에서 만들어진 지역 변수가 아닌 전역 변수의 역할을 한다
    
    for i in range(count): #함수에 count를 입력 받은 만큼 반복
        lock.acquire() #공유 자원인 g_count를 하나가 끝날 때마다 실행되도록 묶어준다
        print("id %s==>count:%s, g_count:%s" %(id, i, g_count))  
        g_count += 1 #for문이 count를 샐 때마다 1씩 늘어나고 id와 count를 입력 받을 때마다 반복한다
        lock.release() #한 번 실행이 끝나면 공유 자원이 다시 실행되도록 풀어준다
        
for i in range(1,6): #이 포문은 1부터 5까지 반복하고 이 for문이 1번 실행될 때마다 threadCount함수의 for문은 5번 실행한다
    Thread(target = threadCount, args = (i, 5)).start() #threadCount 함수에대한 thread로 
    #*target* is the callable object to be invoked by the run()
    #    method. Defaults to None, meaning nothing is called.
    #    *args* is the argument tuple for the target invocation. Defaults to ().
    #Thread.start()
    
time.sleep(1) #join 대신에 사용하여 print가 마지막에 올 수 있도록 한다

#자원을 공유하면서 충돌이 일어날 수도 있다
print("최종 g_count : ", g_count)
print("bye")

