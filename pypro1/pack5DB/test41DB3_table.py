#키보드로 부서번호를 입력하여 해당 부서의 직원 자료 출력

import MySQLdb
"""
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8', #utf-8로 하면 안 된다
    'use_unicode':True #unicode 사용할 거라는 얘기
}
"""

import pickle
with open("mydb.dat", "rb") as obj:
    config = pickle.load(obj)
    
def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        #input으로 키보드로부터 입력값을 받아서 buser_no에 저장하여 sql문에 입력값으로 줌
        buser_no = input("부서번호 입력 : ")
        
        sql = """
            select jikwon_no,jikwon_name,buser_num,jikwon_pay
            from jikwon
            where buser_num={}
        """.format(buser_no)
        #print(sql)
        
        cursor.execute(sql) #이거 뭔지 확인
        
        #하나의 데이터만 읽고 싶으면 fetchone
        datas = cursor.fetchall()
        #print(datas)
        #print(len(datas)) #tuple형식으로 들어오는 데이터의 칼럼 갯수를 알기 위해
        
        if len(datas) == 0:
            print(buser_no + "번 부서는 없습니다.")
            return
        
        for jikwon_no,jikwon_name,buser_num,jikwon_pay in datas:
            print(jikwon_no,jikwon_name,buser_num,jikwon_pay)
            
        print("인원수 : " + str(len(datas)))
        
    except Exception as e:
        print("err : ", e)
    
    finally:
        cursor.close() #cursor 객체 열었던 순서의 역순으로 닫음
        conn.close() #db접속 객체

if __name__ == "__main__":
    chulbal()

