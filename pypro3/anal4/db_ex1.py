#pandas 문제 5)
# MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
#     - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
#     - DataFrame의 자료를 파일로 저장
#     - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
#     - 부서명, 직급으로 교차테이블을 작성(crosstab)
#     - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
#     - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성

import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

#접속 정보를 줄 config 파일을 읽어오기 위해서
try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print("연결 오류 : ", e)


try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    sql= """
        SELECT jikwon_no, jikwon_name, buser_name, jikwon_pay, jikwon_jik
        FROM jikwon
        INNER JOIN buser ON buser_num = buser_no
    """
    cursor.execute(sql)
    
    
    #sql문이 잘 되나 확인
    #for (a, b, c, d, e) in cursor:
    #    print(a, b, c, d, e)
    
    
    #작성한 sql문을 DataFrame으로 작성
    df = pd.DataFrame(cursor.fetchall())
    df.columns = ['번호', '이름', '부서', '연봉', '직급']
    print(df)
    
    
    #작성한 DataFrame을 파일로 저장
    #with open('db_ex_save.csv', mode='w', encoding="UTF-8") as sa:
    #    writer = csv.writer(sa)
    #    for r in cursor:
    #        writer.writerow(r)
    
    
    #부서명별 연봉의 합과 최대 최소값 출력
    a=df.groupby(['부서'])['연봉'].sum()
    b=df.groupby(['부서'])['연봉'].max()
    c=df.groupby(['부서'])['연봉'].min()
        
    print("부서별 연봉의 합: ", a)
    print('-------------')
    print("부서별 연봉의 최대: ", b)
    print('-------------')
    print("부서별 연봉의 최소: ", c)
    print('-------------')
    print("부서별 연봉의 합 : {0}, 최대 연봉 : {1}, 최소 연봉 : {2}".format(a, b, c))
    print('-------------')
    
    #부서명 직급으로 교차 테이블 작성
    ctab = pd.crosstab(df['부서'], df['직급'], margins=True) #margins=True는 전체 소계를 말해준다
    print(ctab)
    
    #ctab1 = pd.crosstab(df['부서'], df['직급'])
    #print(ctab1)
    print('-------------')
    
    #직원별 담당 고객 자료 출력(고객번호, 고객명, 고객전화) 없으면 X로 표시
    sql2 = """
        SELECT jikwon_no, jikwon_name, gogek_no, gogek_name, gogek_tel
        FROM jikwon LEFT OUTER JOIN gogek ON jikwon_no = gogek_damsano
        ORDER BY jikwon_no ASC
    """
    cursor.execute(sql2)
    
    #for (a, b, c, d, e) in cursor:
    #    print(a, b, c, d, e)

    df2 = pd.DataFrame(cursor.fetchall(),
                       columns=['jikwon_no', 'jikwon_name', 'gogek_no', 'gogek_name', 'gogek_tel']).fillna('X')
    #aa=df2.fillna('X')
    print(df2)
    print('-------------')
    #print(df2.loc[:0])
    
    #print(len(df2))
    #print(df2.loc[0])
    #print(range(0, len(df2)))
    #print(df2.loc[:0])
    #print(df2.loc[:len(df2)]["jikwon_name"])
    #print('-------------')
    #print(df2.iloc[:0])
    #print(df2.iloc[:10])
    #print(df2.iloc[:10]["jikwon_name"])
    #for i in range(0, len(df2)+1):
    #    print(df2.iloc[:i])
        #print(len(df2.loc[i]))
        #print()
    #aa = df2.loc[:len(df2)]["jikwon_name"]
    #bb = df2.loc[:len(df2)]["gogek_no"]
    #cc = df2.loc[:len(df2)]["gogek_name"]
    #dd = df2.loc[:len(df2)]["gogek_tel"]
    #for i in range(0, len(df2)+1):
    #    aa = df2.loc[:len(i)]["jikwon_name"]
    #    bb = df2.loc[:len(i)]["gogek_no"]
    #    cc = df2.loc[:len(i)]["gogek_name"]
    #    dd = df2.loc[:len(i)]["gogek_tel"]
    
    #print("담당 직원 : {0}, 고객 번호 : {1}, 고객 이름 : {2}, 고객 전화 번호 : {3}".format(aa, bb, cc, dd))
    
    
    #부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    plt.rc('font', family='malgun gothic') #한글이라 그래프의 한글 깨지니
    
    d=df.groupby(['부서'])['연봉'].mean()
    print(d, type(d))
    plt.barh(range(len(d)), d, alpha = 0.3) #가로 막대는 barh로 하면 된다
    plt.xlabel('연봉(만 원)')
    plt.yticks([0,1,2,3], labels=['관리부', '영업부', '전산부', '총무부'])
    plt.ylabel('부서별')
    plt.show()
    
    
except Exception as e:
    print("처리 오류 : ", e)

finally:
    cursor.close()
    conn.close()











