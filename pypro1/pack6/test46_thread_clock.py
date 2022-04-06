#thread를 이용한 날짜 및 시간 출력

import time

now = time.localtime() #시스템이 가지고 있는 날짜를 얻을 수가 있다

#print(now)
#print(now.tm_year) #시스템상의 연도를 찍을 수가 있다
print(now.tm_year, now.tm_mon, now.tm_mday)

import threading

def calendar_show():
    now = time.localtime()
    print("지금은 {0}년 {1}월 {2}일 {3}시 {4}분 {5}초".format(now.tm_year, now.tm_mon, now.tm_mday,
                                                     now.tm_hour, now.tm_min, now.tm_sec))

#calendar_show()

#a=calendar_show()
#print(a)

def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 11:break #시스템상의 분이 9가 되면 break를 사용
        
        calendar_show()
        time.sleep(1)
        
th = threading.Thread(target = myRun) #myRun() 괄호 주면 X 괄호 열면 실행을 불러오는 것
th.start() #thread를 실행하기 위해서 사용

th.join() #없으면 프로그램 종료가 랜덤적으로 나옴

print("프로그램 종료")






