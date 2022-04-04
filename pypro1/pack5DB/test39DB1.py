#Database 연동 프로그래밍

#개인용 database : sqlite3 - 파이썬에 기본 모듈로 제공됨
import sqlite3
print(sqlite3.sqlite_version)

print()
#conn = sqlite3.connect('exam.db') #경로를 작성해 주지 않으니 현재 모듈과 같은 경로에 만들어짐  DB와 연결
conn = sqlite3.connect(':memory:') #실험용 - ram에 만들어짐 휘발성이라 물리적으로 만들어지지 않음

#DB로 사용할 거면 if문을 써서 데이터 베이스가 있는지 확인하고 넣어야 한다

try: #예외처리는 반드시 하기 해서 나쁠건 없다
    cur = conn.cursor() #SQL문 실행
    #원래는 대문자로 작성해야 하지만 소문자로 작성해도 프로그램 내에서 대문자로 바꿔줌
    #text는 자리수를 안 정해줘도 최대 문자로 잡혀서 상관 없다
    #cur.execute("""create table if not exists friends(name text, phone text, addr text)""") 상관 없음
    #text는 65000자 정도 줌 char(255)까지 varchar는 더 크게 가능 text는 게시판 글 쓰기에 줌
    cur.execute("create table if not exists friends(name text, phone text, addr text)")
    cur.execute("insert into friends values('홍길동', '1111-1111', '서초1동')") #고정 값으로 주는 것
    cur.execute("insert into friends values(?, ?, ?)", ('신기루', '2222-2222', '서초2동')) #데이터 입력값을 바인딩 시켜 주려면 ?를 주고 넣어줌
    inputData = ("신선한", "3333-33333", "서초 2동") #로컬은 ?를 넣음
    cur.execute("insert into friends values(?,?,?)", inputData) #변수에 값을 넣고 바인딩함
    conn.commit()
    
    cur.execute("select * from friends")
    #print(cur.fetchone()) #하나만 읽음
    print(cur.fetchall()) #다 읽음
    
    #입력받은 것을 tuple로 받고 list로 묶음
    #list형식이니 for문으로 돌려서 뽑을 수도 있다
    
    print()
    cur.execute("select * from friends") #없으면??
    for r in cur:
        print(r[0], r[1], r[2])
    
except Exception as e:
    print("err : ", e)
    conn.rollback() #잘못되면 rollback시킴
finally:
    cur.close() #닫는 건 여는 거의 역순으로
    conn.close() #사용이 끝나면 닫자




