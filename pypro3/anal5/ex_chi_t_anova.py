#jikwon 테이블의 자료로 chi2, t-test, ANOVA 정리
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols 
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from astropy.visualization.wcsaxes.tests.test_wcsapi import plt_close


try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)

except Exception as e:
    print("연결 오류 : ", e)

conn = MySQLdb.connect(**config)
cursor = conn.cursor()

print('교차분석 이원 카이제곱 검정 : 각 부서 : 범주형(독립)과 직원 평가점수 : 범주형(종속) 간의 관련성 분석')

#귀무 : 각 부서와 직원 평가 점수 간에 관련이 없다.
#대립 : 각 부서와 직원 평가 점수 간에 관련이 있다.


df= pd.read_sql("SELECT * FROM jikwon", conn)  #jikwon 테이블의 데이터를 읽어올 수가 있다
print(df.head(3))

buser = df['buser_num']
rating = df['jikwon_rating']

ctab = pd.crosstab(buser, rating) #교차표
print(ctab)

chi, p, df, exp = stats.chi2_contingency(ctab)
print('chi:{}, p:{}, df:{}'.format(chi, p, df))
#chi:7.339285714285714, p:0.2906064076671985, df:6
#임계치를 찾아서 chi값이 임계치 안에 있는지 확인한다   -?
#p:0.29060 유의확률 0.05보다 크므로 귀무가설 채택
#각 부서와 직원 평가 점수 간에 관련이 없다.
print("--------------------------------")


print('차이분석(t-검정 : 10번, 20번 부서(범주형 : 독립)와 평균 연봉(연속형 : 종속) 간의 차이 분석')

#귀무(영가설, H0) : 두 부서 간 평균 연봉은 차이가 없다.
#대립(연구가설, H1) : 두 부서 간 평균 연봉은 차이가 있다.

df_10 = pd.read_sql("SELECT buser_num, jikwon_pay from jikwon where buser_num=10", conn)
df_20 = pd.read_sql("SELECT buser_num, jikwon_pay from jikwon where buser_num=20", conn)
buser10 = df_10['jikwon_pay']
buser20 = df_20['jikwon_pay']

print("평균 : ", np.mean(buser10), ' ', np.mean(buser20)) #5414.28571 vs 4908.33333
t_result = stats.ttest_ind(buser10, buser20)
print(t_result)
#Ttest_indResult(statistic=0.4585177708256519, pvalue=0.6523879191675446)
#해석 : p-value는 0.652387로 0.05보다 크므로 귀무가설 채택
#두 부서 간 평균 연봉은 차이가 없다.
print("--------------------------------")


print('분산분석(Anova : 각 부서(요인 1개 : 부서, 4그룹이 존재, 범주형 : 독립)와 평균 연봉(연속형 : 종속) 간의 차이 분석')

#귀무 : 
#대립 : 

df3 = pd.read_sql("SELECT buser_num, jikwon_pay from jikwon", conn)
buser = df3['buser_num']
pay = df3['jikwon_pay']

gr1 = df3[df3['buser_num'] == 10]['jikwon_pay']
gr2 = df3[df3['buser_num'] == 20]['jikwon_pay']
gr3 = df3[df3['buser_num'] == 30]['jikwon_pay']
gr4 = df3[df3['buser_num'] == 40]['jikwon_pay']
#print(gr1)

#시각화
#plt.boxplot([gr1, gr2, gr3, gr4])
#plt.show()

f_sta, pv = stats.f_oneway(gr1, gr2, gr3, gr4)
print('f value : ', f_sta) #0.41244
print('p value : ', pv) #0.74544

#귀무 채택


print("--------------------------------")
#사실상 귀무 채택이라 사후 검정은 안 해도 된다
tukey = pairwise_tukeyhsd(df3.jikwon_pay, df3.buser_num, alpha = 0.05)
print(tukey)

tukey.plot_simultaneous()
plt.show()






