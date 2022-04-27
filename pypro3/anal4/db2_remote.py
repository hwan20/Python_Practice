#원격DB(Maria DB)와 연동처리 : DataFrame
#python으로 연동, Django와는 방식이 다르다

import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc("font", family='malgun gothic')

#config 연결
try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)

except Exception as e:
    print("연결 오류 : ", e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay
        from jikwon inner join buser
        on buser_num = buser_no
    """
    cursor.execute(sql)
    
    #출력 1 : console
    for (a, b, c, d, e, f) in cursor:
        print(a, b, c, d, e, f)
    print('-------------')
    
    
    #출력 2 : DataFrame
    df1 = pd.DataFrame(cursor.fetchall(), columns = ['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_jik', 'jikwon_gen', 'jikwon_pay'])
    print(df1.head(3))
    print('-------------')
    
    #출력 3 : csv 파일로 저장
    '''
    with open('jik_data.csv', mode='w', encoding="UTF-8") as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)
    '''
    
    df2 = pd.read_csv("jik_data.csv", header=None, names=['번호', '이름', '직급', '성별', '연봉'])
    print(df2.head(3))
    print('-------------')
    
    df = pd.read_sql(sql, conn)
    df.columns = ['번호', '이름', '부서', '직급', '성별', '연봉']
    print(df.head(3))
    print('-------------')
    
    #DataFrame에 저장된 자료로 기술통계, 추론통계
    print(df[:3])
    print('-------------')
    print(df[:-27])
    print('-------------')
    
    print('전체 건수 : ', len(df))
    print('이름 건수 : ', df['이름'].count())
    print('-------------')
    
    print("직급별 인원수 : ", df['직급'].value_counts())
    print('-------------')
    
    print("부서별 인원수 : ", df['부서'].value_counts())
    print('-------------')
    
    print("연봉 평균 : ", df.loc[:, '연봉'].sum()/len(df))
    print("연봉 평균 : ", df.loc[:, '연봉'].mean()) #위와 같음
    print('-------------')
    
    print("연봉 표준편차 : ", df.loc[:, '연봉'].std())
    print('-------------')
    
    print(df.loc[:, '연봉'].describe()) #연봉에 대한 정보
    print('-------------')
    
    print(df.loc[df['연봉'] >= 6000]) #연봉이 6000이상인 사람만
    print('-------------')
    
    ctab = pd.crosstab(df['성별'], df['직급'], margins=True) #성별, 직급별 표
    print(ctab)
    print('-------------')
    
    print(df.groupby(['성별', '직급'])['연봉'].count()) #성별과 직급별에 대한 연봉의 수
    print('-------------')
    
    print(df.pivot_table(['연봉'], index=['성별', '직급'], aggfunc = np.mean)) #성별과 직급별 연봉 평균
    print('-------------')
    
    
    #시각화 : pie
    jik_ypay = df.groupby(['직급'])['연봉'].mean() #직급별 평균 연봉
    print(jik_ypay)
    print('-------------')
    
    print(jik_ypay.index)
    print(jik_ypay.values)
    
    plt.pie(x=jik_ypay, explode=(0.2, 0, 0, 0.3, 0), labels=jik_ypay.index,
            shadow=True, labeldistance=0.7, counterclock=False)
    #shadow는 그림자를 줘서 입체적, labeldistance는 라벨의 중심으로부터 위치, counterclock 시계 방향과 반대 방향 어떤 걸로 할지
    plt.show()
    
except Exception as e:
    print("처리 오류 : ", e)

finally:
    cursor.close()
    conn.close()










