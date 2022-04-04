"""
사번과 이름을 입력하여 로그인에 성공하면
사번, 직원명, 부서명, 부서전화, 연봉, 성별 출력
1, 홍길동, 영업부, 123-1234, 12345, 남

buser, jikwon을 join을 사용하여 작성
"""

"""
일반 JOIN 방법
SELECT jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_pay,jikwon_gen
FROM buser, jikwon
WHERE buser_no = buser_num ;
은 WHERE절에 직원의 번호와 이름을 바인딩해서 넣어야 하니 X

ANSI JOIN 방법**
SELECT jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_pay,jikwon_gen
FROM buser
INNER JOIN jikwon ON buser.buser_no = jikwon.buser_num
WHERE = '(?)' AND '(?)' 로 입력 값 바인딩하기

USING JOIN 방법
SELECT jikwon_no,jikwon_name,buser,name,buser_tel,jikwon_pay,jikwon_gen
FROM buser
INNER JOIN jikwon USING(buser_num)
WHERE = '(?)' AND '(?)';
은 join시킬 칼럼의 이름이 달라서 X
부서 테이블은 buser_no이고 jikwon테이블은 buser_num이니

"""

import MySQLdb
import pickle
with open("mydb.dat", "rb") as obj: #sql 아이디와 비밀번호, host 정보 등이 있는 파일 불러오기
    config = pickle.load(obj)
    
def information():
    try:
        conn = MySQLdb.connect(**config) #config의 정보를 tuple 타입으로 입력하기 위해
        cursor = conn.cursor()
        
        j_num = input("사원의 번호 입력 : ")
        j_name = input("사원의 이름 입력 : ")
        
        sql = """
            SELECT jikwon_no,jikwon_name,buser_name,buser_tel,jikwon_pay,jikwon_gen
            FROM buser
            INNER JOIN jikwon ON buser.buser_no = jikwon.buser_num
            WHERE jikwon_no = {0} AND jikwon_name = {1}
        """.format(j_num, "'" + j_name + "'") #이름은 str 타입이고 '' 작은 따옴표 안에 들어가니 

        #print(sql)
        
        cursor.execute(sql) #이거 뭔지 확인
        
        datas = cursor.fetchall() #fetchone()이면 칼럼도 갯수로 처리됨
        #print(datas)
        #print(len(datas))

        if len(datas) == 0:
            print("입력된 정보에 해당하는 사원은 없습니다.")
            return
        
        for jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen in datas:
            print(jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen)
        
        
    except Exception as e:
        print("err : ", e)
    
    finally:
        cursor.close() #cursor 객체 열었던 순서의 역순으로 닫음
        conn.close() #db접속 객체

if __name__ == "__main__": #만약 여기가 메인 문이라면 실행
    information()





