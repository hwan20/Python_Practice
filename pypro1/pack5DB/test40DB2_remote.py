#원격 데이터 베이스 연동
#연결 객체 확인
import MySQLdb

#conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
#print(conn)
#conn.close

#dict 타입
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8', #utf-8로 하면 안 된다
    'use_unicode':True #unicode 사용할 거라는 얘기
}

try:    #위의 config를 작성하지 않으면 connect() 안에 다 넣어줘야 함 packing사용해서 넣어주는데 dict 타입이라 별 2개
    conn = MySQLdb.connect(**config) #Module은 여러 가지가 있을 수가 있지만 connect는 동일
    cursor = conn.cursor()
    
    """
    print("insert ---")
    #isql = "insert into sangdata(code,sang,su,dan) values(10,'신상',5,5000)"
    #isql = "insert into sangdata(code,sang,su,dan) values(%s,%s,%s,%s)"
    isql = "insert into sangdata values(%s,%s,%s,%s)" #들어오는 순서가 같으면 칼럼 명 안 써도 상관 X
    #입력 받아서 사용하는 식으로 해야 web에서 데이터를 받고 db에 넣을 수가 있다
    sql_data = (10,'신상',5,5000) #tuple타입 가독성이 좋게 하기 위해 괄호 작성
    #sql_data = 10,'신상',5,5000 #이것도 tuple타입
    
    #바인딩 해서 넣음 이렇게 작성하면 일부만 읽어서 가져옴
    cursor.execute(isql, sql_data) #성공하면 1을 실패하면 0을 반환함. 반환 된 값을 갖고 성공 여부를 가질 수 있다
    #err :  (1062, "Duplicate entry '10' for key 'PRIMARY'") commit하고 난 후 또 실행하면 primary key error가 걸림
    conn.commit() #commit을 해줘야 연동됨 java와 반대
    """
    
    """
    print("update ---")
    usql = "update sangdata set sang=%s, su=%s where code=%s"
    sql_data = ("얼죽아",30,10)
    cou = cursor.execute(usql, sql_data)
    print("cou : ",cou) #성공하면 1을 실패하면 0을 반환함. 반환 된 값을 갖고 성공 여부를 가질 수 있다
    conn.commit()
    """
    
    """
    print("delete ---")
    input_code = "10"
    #dsql = "delete from sangdata where code=" + input_code #secure coding 가이드 라인에 위배됨 +가 붙으면 해킹 당할 위험 큼
    
    #이런 식으로 넣어야 가이드 라인에 알맞음
    #dsql = "delete from sangdata where code=%s"
    #cou = cursor.execute(dsql,(input_code,))
    
    #이렇게 사용할 수도 있다 맷핑 해서 넣으라는 뜻
    dsql = "delete from sangdata where code='{0}'".format(input_code)
    cou = cursor.execute(dsql) #tuple값으로 바인딩해서 넣음
    
    #리턴되는 값을 이용해서 조절할 수가 있다
    if cou > 0: #마땅히 넣을 게 없어서 대충 넣은 것
        print("삭제 성공")
    else:
        print("삭제 실패")
    conn.commit()
    """
    
    print("select ---")
    sql = "select code,sang,su,dan from sangdata"
    cursor.execute(sql) #sql을 읽은것 2개 이상을 동시에 참조하는 것은 없다
    
    #아래 모두 상관 없다
    for data in cursor.fetchall():
        #print(data)
        print("%s %s %s %s" %data)
    """
    print()
    for data in cursor:
        print(data[0], data[1], data[2], data[3])
        
    print() #칼럼이 아니고 변수명
    for (code, sang, su, dan) in cursor:
        print(code, sang, su, dan)
        
    print()
    for (a, b, c, d) in cursor:
        print(a, b, c, d)
    
    """
    
    
#except MySQLdb.connections.Error as e: #이렇게 하면 db연동시 나오는 에러를 더 구체적이게 볼 수가 있다
#    if e.errno == errcode.ER_ACC

except Exception as e:
    print("err : ", e)
    
finally:
    cursor.close()
    conn.close()








