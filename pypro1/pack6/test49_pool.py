#python에서는 multi process로 thread대신 pool을 사용한다
#thread는 python에서 GIL이라는 메커니즘 때문에 완전한 multi process가 불가능하다
#멀티 프로세싱을 위한 pool process 클래스를 별도로 지원한다

#pool 클래스
from multiprocessing import Pool
import time
import os

def pool_func(arg):
    print("값", arg, "에 대한 pid:", os.getpid()) #현재 실행되는 process id를 출력 작업 관리자에서 관리하는 데이터 내용
    time.sleep(1) #처리가 빠르면 보기 힘드니
    return arg + 10

#pool_func(2) #실행 될 때마다 process id를 같이 찍음

if __name__ == "__main__":
    startTime = int(time.time()) #처리 시간 체크용으로 startTime 변수를 줌
    
    #방법 1: pool 객체를 사용하지 않은 상태로 함수 호출하기
    """
    for i in range(10):
        pool_func(i) #process id를 하나만 사용
        print(pool_func(i))
    endTime = int(time.time())
    """
    
    #방법 2: Pool 객체를 사용해서 함수 호출
    po = Pool(processes = 2) #pool에서 프로세스의 개수는 3~5가 적당(권장)
    print(po.map(pool_func, range(10))) #4시 51분 함수명과 아규먼트(인자)를 전달
    endTime = int(time.time())
    
    #동일한 작업을 병렬 처리로 시작해서 작업 속도가 더욱 빨라짐
    
    print("총 작업 시간 : ", (endTime - startTime))





