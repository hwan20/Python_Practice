"""
지금껏 A회사의 직급과 연봉은 관련이 없다. 
그렇다면 정말로 jikwon_jik과 jikwon_pay 간의 관련성이 없는지 분석. 가설검정하시오.
  예제파일 : MariaDB의 jikwon table 
  jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
  jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
  조건 : NA가 있는 행은 제외한다.
"""
import MySQLdb
import pickle
import pandas as pd
import scipy.stats as stats

#귀무가설 : A회사의 직급과 연봉은 관련이 없다 (독립이다)
#대립가설 : A회사의 직급과 연봉은 관련이 있다 (종속적이다)

try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)

except Exception as e:
    print("연결 오류 : ", e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        SELECT jikwon_jik, jikwon_pay
        FROM jikwon
        ORDER BY jikwon_jik ASC 
    """
    cursor.execute(sql)
    
    #for (a, b) in cursor:
    #    print(a,b)
    
    df = pd.DataFrame(cursor.fetchall(), columns=['jikwon_jik', 'jikwon_pay']).dropna()
    print(df)
    bins=[1000, 2999, 4999, 6999, 10000]
    labels = [1, 2, 3, 4]
    df['jik_pay'] = pd.cut(df['jikwon_pay'], bins=bins, labels=labels, right=True)
    #print(df['jik_pay'])
    
    ctab = pd.crosstab(index=df['jikwon_jik'], columns=df['jik_pay'])
    ctab.index = ['3', '4', '2', '5', '1']
    ctab.columns = ['1000~2999', '3000~4999', '5000~6999', '7000~']
    #print(ctab)
    #print()
    ctab2 = ctab.reindex(index=['1', '2', '3', '4', '5'])
    print(ctab2)
    
    chi2, p, ddof, _ = stats.chi2_contingency(ctab2)
    print("chi2 : {}, p : {}, ddof : {}".format(chi2, p, ddof))
    #chi2 : 37.40349394195548, p : 0.00019211533885350577, df : 12      chi2와 p는 반비례관계
    #p값이 0.00019로 유의 수준 0.05보다 낮으므로 귀무가설은 기각하고 대립가설은 채택된다
    
    #카이제곱분포표로 확인
    #검정통계량 chi2의 값은 37.40349이고 자유도는 4일때 카이제곱분포표에 나와있는 임계값은 9.49이다
    #이때 검정통계량 값이 임계값 9.49보다 높으므로 귀무가설을 기각하고 대립가설을 채택한다
    
    #A회사의 직급과 연봉은 관련이 있다
    
except Exception as e:
    print('처리 오류 : ', e)

finally:
    cursor.close()
    conn.close()






